from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    LoginView,
    LogoutView,
    PasswordRecoveyView,
    PasswordResetView,
    RegisterView,
    VerifyEmailView,
)


urlpatterns = [
    path(r"token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(r"token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(r"token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(r"register/", RegisterView.as_view(), name="register"),
    path(r"email/verify/", VerifyEmailView.as_view(), name="verify-email"),
    path(r"login/", LoginView.as_view(), name="login"),
    path(r"logout/", LogoutView.as_view(), name="logout"),
    path(
        r"password/recovery/", PasswordRecoveyView.as_view(), name="password-recovery"
    ),
    path(r"password/reset/", PasswordResetView.as_view(), name="password-reset"),
]
