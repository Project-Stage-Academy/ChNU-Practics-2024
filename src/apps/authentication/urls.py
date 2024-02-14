from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

<<<<<<< HEAD
from .views import RegisterView
from .views import VerifyEmailView
||||||| parent of 4625cf7 (Implementing new feature or fixing issue)
from .views import RegisterView
=======
from .views import RegisterView, LogoutApiView
>>>>>>> 4625cf7 (Implementing new feature or fixing issue)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(r"register/", RegisterView.as_view(), name="register"),
<<<<<<< HEAD
    path(r"email/verify/", VerifyEmailView.as_view(), name="verify-email"),
||||||| parent of 4625cf7 (Implementing new feature or fixing issue)
=======
    path("logout/", LogoutApiView.as_view(), name="logout"),
>>>>>>> 4625cf7 (Implementing new feature or fixing issue)
]
