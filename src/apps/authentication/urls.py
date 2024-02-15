from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from .views import PasswordRecoveyView
from .views import PasswordResetView
from .views import RegisterView
from .views import VerifyEmailView


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(r"register/", RegisterView.as_view(), name="register"),
    path(r"email/verify/", VerifyEmailView.as_view(), name="verify-email"),
    path(
        r"password/recovery/", PasswordRecoveyView.as_view(), name="password-recovery"
    ),
    path(r"password/reset/", PasswordResetView.as_view(), name="password-reset"),
]
