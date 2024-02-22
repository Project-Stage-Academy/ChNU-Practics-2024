from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Founder, Investor, Role, User
from .permissions import IsAdminOrSelf, IsFounder, IsInvestor
from .serializers import FounderSerializer, InvestorSerializer, UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSelf]

    def get_queryset(self):
        return (
            User.objects.filter(id=self.request.user.id)  # type: ignore
            if not self.request.user.is_superuser  # type: ignore
            else User.objects.all()
        )


class RoleBasedListVIew(generics.ListAPIView):
    serializer_class = None
    permission_classes = None
    model = None

    def get_queryset(self):
        if self.model:
            return self.model.objects.all()
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class InvestorListView(RoleBasedListVIew):
    serializer_class = InvestorSerializer  # type: ignore
    permission_classes = [IsFounder]  # type: ignore
    model = Investor  # type: ignore


class FounderListView(RoleBasedListVIew):
    serializer_class = FounderSerializer  # type: ignore
    permission_classes = [IsInvestor]  # type: ignore
    model = Founder  # type: ignore


class SwitchRoleView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.role = Role.INVESTOR if user.role == Role.STARTUP else Role.STARTUP
        user.save()
        return Response(UserSerializer(user).data)
