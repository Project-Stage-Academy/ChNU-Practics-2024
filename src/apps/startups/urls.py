from django.contrib import admin
from django.urls import include, path

from .views import (
    startup_profile_view,
)


urlpatterns = [
    path("<uuid:startup_id>/", startup_profile_view, name="startup_profile"),
]
