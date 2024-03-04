from rest_framework import serializers

from apps.users.models import Founder

from .models import Startup


class StartupSerializer(serializers.ModelSerializer):
    founders = serializers.PrimaryKeyRelatedField(queryset=Founder.objects.all(), many=True)


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
