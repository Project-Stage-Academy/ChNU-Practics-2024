from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Founder, Investor, Role, User
from .permissions import IsAdminOrSelf, IsFounder, IsInvestor
from .serializers import FounderSerializer, InvestorSerializer, UserSerializer


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSelf]

    def get_queryset(self):
        return (
            User.objects.filter(id=self.request.user.id)  # type: ignore
            if not self.request.user.is_superuser  # type: ignore
            else User.objects.all()
        )

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class InvestorListView(ListAPIView):
    serializer_class = InvestorSerializer
    permission_classes = [IsFounder]

    def list(self, request, *args, **kwargs):
        queryset = Investor.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FounderListView(ListAPIView):
    serializer_class = FounderSerializer
    permission_classes = [IsInvestor]

    def list(self, request, *args, **kwargs):
        queryset = Founder.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SwitchRoleView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.role = Role.INVESTOR if user.role == Role.STARTUP else Role.STARTUP
        user.save()
        return Response(UserSerializer(user).data)
