import jwt
from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .serializers import RegisterSerializer
from .utils import get_user_from_token
from .utils import send_confirmation_email


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

        try:
            user = get_user_from_token(token)
            self.verify_user_email(user)

            return Response(
                {"message": "Email verified successfully"}, status=status.HTTP_200_OK
            )

        except jwt.ExpiredSignatureError:
            raise APIException(
                detail="Token expired", code=status.HTTP_400_BAD_REQUEST
            ) from None
        except jwt.DecodeError:
            raise APIException(
                detail="Token invalid", code=status.HTTP_400_BAD_REQUEST
            ) from None

    def verify_user_email(self, user):
        user.is_verified = True
        user.save()
