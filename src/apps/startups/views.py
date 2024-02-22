from django.shortcuts import get_object_or_404, render
from rest_framework import filters, generics, viewsets

from apps.users.permissions import IsInvestor

from .models import Startup
from .serializers import StartupSerializer


class StartupViewSet(viewsets.ModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


def startup_profile_view(request, startup_id):
    startup = get_object_or_404(Startup, id=startup_id)

    for founder in startup.founders.all():
        print(founder)

    return render(request, "startup_profile.html", {"startup": startup})


class StartupSearchView(generics.ListAPIView):
    serializer_class = StartupSerializer
    permission_classes = [IsInvestor]
    filter_backends = [filters.SearchFilter]
    search_fields = ["company_name", "founders__name", "location"]
    filterset_fields = ["industry", "location", "size"]

    def get_queryset(self):  # type: ignore
        return Startup.objects.filter(is_active=True)
