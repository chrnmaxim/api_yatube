from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    """Permission to modify the author's content."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated
               )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
