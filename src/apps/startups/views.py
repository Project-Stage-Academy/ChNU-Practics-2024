from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response

from .models import Startup
from .serializers import (
    StartupSerializer,
)


class StartupViewSet(generics.GenericAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer



def startup_profile_view(request, startup_id):
    startup = get_object_or_404(Startup, id=startup_id)
    return render(request, "startup_profile.html", {"startup": startup})
