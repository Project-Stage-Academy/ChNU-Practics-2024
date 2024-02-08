from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.views import UserRegisterView


router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path(r"auth/register/", UserRegisterView.as_view(), name="user-register"),
]
