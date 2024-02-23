from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Founder, Investor, Role, User
from .permissions import IsAdminOrSelf, IsFounder, IsInvestor
from .serializers import FounderSerializer, InvestorSerializer, UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSelf]
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            self.queryset = User.objects.filter(id=request.user.id)

        return super().list(request, *args, **kwargs)


class InvestorListView(ListAPIView):
    serializer_class = InvestorSerializer
    permission_classes = [IsFounder]
    queryset = Investor.objects.filter(is_active=True)


class FounderListView(ListAPIView):
    serializer_class = FounderSerializer
    permission_classes = [IsInvestor]
    queryset = Founder.objects.filter(is_active=True)


class SwitchRoleView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.role != Role.BOTH:
            user.role = Role.INVESTOR if user.role == Role.STARTUP else Role.STARTUP
            user.save()
        return Response(UserSerializer(user).data)
