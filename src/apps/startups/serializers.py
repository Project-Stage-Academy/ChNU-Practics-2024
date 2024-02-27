from rest_framework import serializers

from apps.users.serializers import FounderSerializer

from .models import Startup


class StartupSerializer(serializers.ModelSerializer):
    founders = FounderSerializer(many=True, read_only=True)

    class Meta:
        model = Startup
        fields = "__all__"


class FilteredStartupSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="startup_profile", lookup_field="pk"
    )

    class Meta:
        model = Startup
        fields = ["company_name", "location", "size", "created_at", "url"]
