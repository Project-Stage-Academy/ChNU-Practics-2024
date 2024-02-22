from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import (
    startup_profile_view,
    StartupListAPIView,
    StartupRetrieveUpdateAPIView,
    # StartupRetrieveAPIView,
    # StartupUpdateAPIView,
    StartupViewSet,
)


router = routers.DefaultRouter()
router.register("", StartupViewSet)


urlpatterns = [
    path("<uuid:startup_id>/", startup_profile_view, name="startup_profile"),
    path("", StartupListAPIView.as_view(), name="startup_list"), 
    path("<uuid:id>/update/", StartupRetrieveUpdateAPIView.as_view(), name="startup_update"),
]

urlpatterns += router.urls

