from rest_framework.throttling import SimpleRateThrottle

from App.models import UserModel
# from App.views import UserAPIView


class UserThrottle(SimpleRateThrottle):
    # scope 對應的是 settings.py 的 REST_FRAMEWORK.DEFAULT_THROTTLE_RATES 的  key: user
    scope = 'user'

    def get_cache_key(self, request, view):
        print(view)
        # if isinstance(view, UserAPIView):
        #     print('in')
        if isinstance(request.user, UserModel):
            ident = request.auth
            print(ident)
        else:
            ident = self.get_ident(request)
        return f'throttle_{self.scope}_{ident}'
        # 下面的是原檔的。
        # return self.cache_format % {
        #     'scope': self.scope,
        #     'ident': ident
        # }


class AddressThrottle(SimpleRateThrottle):
    # scope 對應的是 settings.py 的 REST_FRAMEWORK.DEFAULT_THROTTLE_RATES 的  key: user
    scope = 'address'

    def get_cache_key(self, request, view):
        if isinstance(request.user, UserModel):
            ident = request.auth
        else:
            ident = self.get_ident(request)
        return f'throttle_{self.scope}_{ident}'
