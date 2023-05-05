from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsUserColaboratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_librarian:
            return True

        return False