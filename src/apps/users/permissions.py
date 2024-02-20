from rest_framework import permissions

from .models import Role


class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj == request.user


class IsInvestor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.INVESTOR


class IsFounder(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.STARTUP
