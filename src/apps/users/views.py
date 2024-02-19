from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Role, User
from .permissions import IsAdminOrSelf
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSelf]

    def list(self, request):
        users = (
            User.objects.filter(id=request.user.id)
            if not request.user.is_superuser
            else User.objects.all()
        )

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)


class SwitchRoleView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.role = Role.INVESTOR if user.role == Role.STARTUP else Role.STARTUP
        user.save()
        return Response(UserSerializer(user).data)
