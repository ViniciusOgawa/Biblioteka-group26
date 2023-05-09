from rest_framework import permissions
from users.models import User
from rest_framework.views import View


class IsLybrarian(permissions.BasePermission):
    def has_permission(self, request, view: View, obj: User) -> bool:
        if request.user.is_authenticated and request.user.is_librarian == True:
            return True
        return False
