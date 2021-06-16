from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from App.models import UserModel


class LoginAuthentications(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        user_id = cache.get(token)
        try:
            user = UserModel.objects.get(pk=user_id)
            return user, token
        except UserModel.DoesNotExist:
            return
