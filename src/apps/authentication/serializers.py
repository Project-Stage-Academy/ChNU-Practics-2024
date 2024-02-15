from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.users.models import User

from .mixins import CreateUserMixin, TokenHandlerMixin, ValidatePasswordMixin


class RegisterSerializer(
    serializers.ModelSerializer, ValidatePasswordMixin, CreateUserMixin
):
    password1 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "password1",
            "first_name",
            "last_name",
            "role",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, vaslidated_data):
        return self.create_user(vaslidated_data)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        self.validate_password_match(attrs["password"], attrs["password1"])
        return attrs


class LogoutSerializer(serializers.Serializer, TokenHandlerMixin):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs.get("refresh")
        return super().validate(attrs)

    def save(self):
        self.blacklist_token(self.token)


class LoginSerializer(serializers.Serializer, TokenHandlerMixin):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )

            if user:
                attrs["user"] = user
            else:
                raise serializers.ValidationError(
                    "Unable to log in with provided credentials."
                )
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        return super().validate(attrs)


class PasswordRecoverySerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        attrs = super().validate(attrs)

        try:
            attrs["user"] = User.objects.get(email=attrs["email"])
        except User.DoesNotExist as exc:
            raise serializers.ValidationError(
                "User with this email does not exist."
            ) from exc
        return attrs


class PasswordResetSerializer(serializers.Serializer, ValidatePasswordMixin):
    new_password = serializers.CharField(write_only=True, required=True)
    new_password1 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        self.validate_password_match(attrs["new_password"], attrs["new_password1"])
        return attrs
