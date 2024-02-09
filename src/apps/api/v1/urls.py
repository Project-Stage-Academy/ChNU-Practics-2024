from django.urls import include
from django.urls import path


urlpatterns = [
    path("auth/", include("apps.authentication.urls")),
]
