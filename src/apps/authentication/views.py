from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LogoutSerializer
from .serializers import PasswordRecoverySerializer
from .serializers import PasswordResetSerializer
from .serializers import RegisterSerializer
from .serializers import UserLoginSerializer
from .utils import decode_token
from .utils import send_confirmation_email
from .utils import send_password_recovery_email


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

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


class LogoutApiView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return None

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(
                request,
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )

            if user is not None:
                login(request, user)

                return Response(
                    data=serializer.validated_data, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": "Authentication failed"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
