from django.conf import settings
import jwt
from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from apps.users.models import User

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, requst, *args, **kwargs):
        return self.create(requst, *args, **kwargs)

    def perform_create(self, serializer):
        user = serializer.save()
        serializer.send_confirmation_email(user)


class VerifyEmailView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        token = request.query_params.get("token")

        try:
            user = self._get_user_from_token(token)
            self._verify_user_email(user)

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

    def _get_user_from_token(self, token):
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT["ALGORITHM"]
        )
        return User.objects.get(id=payload["user_id"])

    def _verify_user_email(self, user):
        user.is_verified = True
        user.save()
