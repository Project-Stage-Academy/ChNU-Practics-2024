from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Register your API routes here

urlpatterns = [
    path("", include(router.urls)),
]
