from rest_framework import serializers

from .models import Startup
from apps.users.serializers import FounderSerializer


class StartupSerializer(serializers.ModelSerializer):
    founders = FounderSerializer(many=True)
    class Meta:
        model = Startup
        fields = "__all__"
