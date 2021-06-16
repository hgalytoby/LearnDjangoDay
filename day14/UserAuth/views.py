import uuid

from django.core.cache import cache
from django.shortcuts import render

# Create your views here.

from rest_framework import status, exceptions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from UserAuth.auth import UserAuth
from UserAuth.constants import HTTP_ACTION_REGISTER, HTTP_ACTION_LOGIN
from UserAuth.models import UserModel
from UserAuth.permissions import IsAdmin
from UserAuth.serializers import UserSerializer
from project.settings import SUPER_USERS


class UsersAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = (UserAuth,)
    permission_classes = (IsAdmin, )

    # def get(self, request, *args, **kwargs):
    #     if isinstance(request.user, UserModel):
    #         return self.list(request, *args, **kwargs)
    #     raise exceptions.NotAuthenticated

    def post(self, request, *args, **kwargs):
        # 文檔 code。
        # query_params.get('action') 是屬於 GET 的行為，是抓 url 網址後面的 ?action=login
        action = request.query_params.get('action')
        if action == HTTP_ACTION_REGISTER:
            # return 抄文檔。
            return self.create(request, *args, **kwargs)

        elif action == HTTP_ACTION_LOGIN:
            u_name = request.data.get('u_name')
            u_password = request.data.get('u_password')
            try:
                user = UserModel.objects.get(u_name=u_name)
                if user.u_password == u_password:
                    token = uuid.uuid4().hex
                    cache.set(token, user.id)
                    data = {
                        'msg': 'login success',
                        'status': 200,
                        'token': token
                    }
                    return Response(data)
                raise exceptions.AuthenticationFailed
            except UserModel.DoesNotExist:
                raise exceptions.NotFound
        raise exceptions.ValidationError

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # 原碼 copy
        self.perform_create(serializer)
        data = serializer.data
        u_name = request.data.get('u_name')
        if u_name in SUPER_USERS:
            u_id = data.get('id')
            user = UserModel.objects.get(pk=u_id)
            user.is_super = True
            user.save()
            data.update({'is_super': True})
        print(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
