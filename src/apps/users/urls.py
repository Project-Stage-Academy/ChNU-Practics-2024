from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SwitchRoleView, UserViewSet


router = DefaultRouter()

router.register(r"", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<uuid:pk>/switch-role/", SwitchRoleView.as_view(), name="switch-role"),
]
