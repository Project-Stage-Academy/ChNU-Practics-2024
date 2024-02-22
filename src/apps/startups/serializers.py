from rest_framework import serializers

from apps.users.models import Founder
from apps.users.serializers import FounderSerializer

from .models import Startup


class StartupSerializer(serializers.ModelSerializer):
    #founders = FounderSerializer(many=True)
    founders = serializers.PrimaryKeyRelatedField(queryset=Founder.objects.all(), many=True)

    class Meta:
        model = Startup
        fields = "__all__"
