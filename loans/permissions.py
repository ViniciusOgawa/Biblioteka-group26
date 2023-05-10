from rest_framework import permissions


class IsUserColaboratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_librarian:
            return True

        return False
