from django.contrib.auth import login
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    LoginSerializer,
    LogoutSerializer,
    PasswordRecoverySerializer,
    PasswordResetSerializer,
    RegisterSerializer,
)
from .utils import decode_token, send_user_email


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_user_email(self.request, user, "Verify Email", "verify-email")


class VerifyEmailView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        token = request.query_params.get("token")

        user = decode_token(token)
        self.verify_user_email(user)

        return Response(
            {"message": "Email verified successfully"}, status=status.HTTP_200_OK
        )

    def verify_user_email(self, user):
        user.is_verified = True
        user.save()


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        login(request, user)

        refresh = RefreshToken.for_user(user)
        data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "access": str(refresh.access_token),  # type: ignore
            "refresh": str(refresh),
        }

        return Response(data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    queryset = []  # type: ignore
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PasswordRecoveyView(generics.GenericAPIView):
    serializer_class = PasswordRecoverySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        send_user_email(request, user, "Password Recovery", "password-reset")

        return Response(
            {"message": "Password recovery email sent successfully"},
            status=status.HTTP_200_OK,
        )


class PasswordResetView(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = request.query_params.get("token")
        user = decode_token(token)

        user.set_password(serializer.validated_data["new_password"])
        user.save()

        return Response(
            {"message": "Password reset successfully"}, status=status.HTTP_200_OK
        )
