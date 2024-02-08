from django.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from apps.users.views import UserRegisterView


router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r"auth/register/", UserRegisterView.as_view(), name="user-register"),
]
