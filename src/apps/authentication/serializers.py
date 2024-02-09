from django.contrib.auth.password_validation import validate_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User
from apps.users.models import UserRole

from .utils import send_email


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

    def send_confirmation_email(self, user):
        link = self.get_verification_link(user)
        send_email(
            "Verify your email address",
            f"Click the link to verify your email address: {link}",
            [user.email],
        )

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

    def get_verification_link(self, user):
        current_site = get_current_site(self.context["request"])
        verify_link = reverse("verify-email")
        token = RefreshToken.for_user(user)
        access_token = str(token.access_token)
        return f"http://{current_site}{verify_link}?token={access_token}"
