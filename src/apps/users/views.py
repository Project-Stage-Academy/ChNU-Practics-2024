from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .permissions import IsAdminOrSelf
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSelf]

    def list(self, request):
        if request.user.is_superuser:
            users = User.objects.all()
        elif request.user.role == "investor":
            users = User.objects.filter(role__in=["investor", "both"])
        elif request.user.role == "startup":
            users = User.objects.filter(role__in=["startup", "both"])
        else:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=403,
            )

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user != self.get_object():
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=403,
            )

        return super().update(request, *args, **kwargs)


class SwitchRoleView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.role = "investor" if user.role == "startup" else "startup"
        user.save()
        return Response(UserSerializer(user).data)
