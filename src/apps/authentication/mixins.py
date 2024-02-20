from django.contrib.auth.password_validation import validate_password
from django.core.cache import cache
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


class ValidatePasswordMixin:
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(exc.messages) from exc

        return value

    def validate_password_match(self, password1, password2):
        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match.")


class CreateUserMixin:
    def create_user(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(**validated_data)


class TokenHandlerMixin:
    @staticmethod
    def blacklist_token(refresh_token):
        try:
            RefreshToken(refresh_token).blacklist()
        except TokenError as err:
            raise serializers.ValidationError("Token is invalid or expired.") from err

    @staticmethod
    def blacklist_access(access_token):
        # Add the access token to the cache with a timeout of 5 minutes,
        # preventing its reuse within that time frame, aligning with the token expiration set in our application settings.
        cache.set(access_token, "true", timeout=60 * 5)
