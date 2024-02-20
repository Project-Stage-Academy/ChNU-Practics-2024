from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
import jwt
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


def send_email(subject: str, message: str, recipient_list: list[str]) -> None:
    if all([settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD, recipient_list]):
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)


def generate_verification_link(request, user, path_name: str) -> str:
    domain = get_current_site(request).domain
    token = RefreshToken.for_user(user)
    access_token = str(token.access_token)  # type: ignore
    return f"http://{domain}{reverse(path_name)}?token={access_token}"


def send_user_email(request, user, subject: str, path_name: str) -> None:
    link = generate_verification_link(request, user, path_name)
    send_email(subject, f"Click the link to {subject.lower()}: {link}", [user.email])


def get_user_from_token(token):
    payload = jwt.decode(
        token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT["ALGORITHM"]
    )
    return User.objects.get(id=payload["user_id"])


def decode_token(token):
    try:
        user = get_user_from_token(token)
        return user
    except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
        raise APIException(
            detail="Token invalid or expired", code=status.HTTP_400_BAD_REQUEST
        ) from None
