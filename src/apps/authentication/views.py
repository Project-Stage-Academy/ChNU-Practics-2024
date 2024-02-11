from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializers import PasswordRecoverySerializer
from .serializers import PasswordResetSerializer
from .serializers import RegisterSerializer
from .utils import decode_token
from .utils import send_confirmation_email
from .utils import send_password_recovery_email


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = serializer.save()
        send_confirmation_email(self.request, user)


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


class PasswordRecoveyView(generics.GenericAPIView):
    serializer_class = PasswordRecoverySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        send_password_recovery_email(request, user)

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
