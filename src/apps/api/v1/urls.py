from django.urls import include, path


urlpatterns = [
    path("auth/", include("apps.authentication.urls")),
    path("users/", include("apps.users.urls")),
    path("startup/", include("apps.startups.urls")),
]
