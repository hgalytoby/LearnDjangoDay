from rest_framework.permissions import BasePermission

from UserAuth.models import UserModel


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            if isinstance(request.user, UserModel):
                return request.user.is_super
            return False
        return True
