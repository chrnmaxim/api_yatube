from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    """Разрешение для изменения контента автора."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )