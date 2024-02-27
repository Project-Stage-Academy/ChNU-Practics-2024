from django.shortcuts import get_object_or_404, render
from rest_framework import filters, generics, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.permissions import IsInvestor

from .models import Startup
from .serializers import FilteredStartupSerializer, StartupSerializer


class StartupViewSet(viewsets.ModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


def startup_profile_view(request, pk):
    startup = get_object_or_404(Startup, id=pk)
    return render(request, "startup_profile.html", {"startup": startup})


class SearchStartupView(generics.ListAPIView):
    serializer_class = FilteredStartupSerializer
    permission_classes = [IsAuthenticated, IsInvestor]
    filter_backends = [filters.SearchFilter]
    search_fields = ["company_name", "location"]
    filterset_fields = ["location", "size"]

    def get_queryset(self):  # type: ignore
        queryset = Startup.objects.filter(is_active=True)

        location = self.request.query_params.get("location")
        size = self.request.query_params.get("size")

        if location:
            queryset = queryset.filter(location__icontains=location)
        if size:
            queryset = queryset.filter(size=size)

        return queryset
