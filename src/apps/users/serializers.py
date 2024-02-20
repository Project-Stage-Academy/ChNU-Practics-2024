from rest_framework import serializers

from .models import Founder, Investor, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        ]


class InvestorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Investor
        fields = "__all__"


class FounderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Founder
        fields = "__all__"
