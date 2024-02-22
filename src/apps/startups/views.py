from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from .models import Startup
from .serializers import (
    StartupSerializer,
)


class StartupRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "id"

class StartupViewSet(viewsets.ModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


class StartupListAPIView(generics.ListCreateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def startup_profile_view(request, startup_id):
    startup = get_object_or_404(Startup, id=startup_id)

    for founder in startup.founders.all():
        print(founder)

    return render(request, "startup_profile.html", {"startup": startup})
