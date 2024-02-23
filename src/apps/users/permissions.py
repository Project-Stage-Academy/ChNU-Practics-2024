from rest_framework import permissions

from .models import Role


class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj == request.user


class HasRole(permissions.BasePermission):
    role = None

    def has_permission(self, request, view):
        user_role = request.user.role
        return user_role == self.role or user_role == Role.BOTH


class IsInvestor(HasRole):
    role = Role.INVESTOR


class IsFounder(HasRole):
    role = Role.STARTUP
