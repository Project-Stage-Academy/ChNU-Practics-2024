from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from apps.users.models import User
from apps.users.models import UserRole


class RegisterSerializer(serializers.ModelSerializer):
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

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1")
        user = User.objects.create_user(**validated_data)

        role = validated_data.pop("role", None)
        self.set_user_role(user, role)

        return user

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(exc.messages) from exc

        return value

    def validate_password1(self, value):
        data = self.get_initial()
        password = data.get("password")

        if password != value:
            raise serializers.ValidationError("Passwords do not match.")

        return value

    def set_user_role(self, user, role):
        if role and role != UserRole.ADMIN:
            user.role = role
            user.save()


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {"bad_token": "Token is invalid."}

    def validate(self, attrs):
        self.token = attrs("refresh")

        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail("bad_token")


class UserLoginSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = User.objects.get(email=email)
            if not user:
                raise serializers.ValidationError("User not found")

            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect password")

            refresh_token = RefreshToken.for_user(user)

            attrs["access_token"] = str(refresh_token.access_token)
            attrs["id"] = user.id
            attrs["username"] = user.username

            return attrs
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")


class PasswordRecoverySerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        attrs = super().validate(attrs)

        attrs["user"] = User.objects.get(email=attrs["email"])

        return attrs

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist as exc:
            raise serializers.ValidationError(
                "User with this email does not exist."
            ) from exc

        return value


class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True)
    new_password1 = serializers.CharField(write_only=True, required=True)

    def validate_new_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(exc.messages) from exc

        return value

    def validate_new_password1(self, value):
        data = self.get_initial()
        new_password = data.get("new_password")

        if new_password != value:
            raise serializers.ValidationError("Passwords do not match.")

        return value

