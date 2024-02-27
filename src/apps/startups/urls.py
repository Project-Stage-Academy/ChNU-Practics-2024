from django.urls import path
from rest_framework import routers

from .views import SearchStartupView, startup_profile_view, StartupViewSet


router = routers.DefaultRouter()
router.register("", StartupViewSet)


urlpatterns = [
    path("<uuid:pk>/", startup_profile_view, name="startup_profile"),
    path("search/", SearchStartupView.as_view(), name="search_startup"),
]

urlpatterns += router.urls
