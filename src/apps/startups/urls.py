from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import (
    startup_profile_view,
    StartupViewSet
)
router = routers.DefaultRouter()
router.register("", StartupViewSet)


urlpatterns = [
    path("<uuid:startup_id>/", startup_profile_view, name="startup_profile"),
]

urlpatterns += router.urls

