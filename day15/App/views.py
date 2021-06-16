import uuid

from django.contrib.auth.models import User, Group
from django.shortcuts import render

# Create your views here.
from rest_framework import exceptions, status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.cache import cache

from App.auth import LoginAuthentications
from App.models import UserModel, Address, Test
from App.permissions import RequireLoginPermission
from App.serializers import UserSerializer, AddressSerializer, TestSerializer, SuperSerializer, GroupSerializer
from App.throttles import UserThrottle


class UsersAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get(self, request, *args, **kwargs):
        # url 最後面加入?page=1 or 2 ...就可以換分頁資料。
        pg_obj = PageNumberPagination()  # 實例化分頁類。
        # 取得分頁資料，參數1 分頁的資料，Queryset類型，請求request，分頁的視圖，self代表自己
        pg_res = pg_obj.paginate_queryset(queryset=self.queryset, request=request, view=self)
        # 報錯訊息提示要加入 context={'request': request}，好像因為有關連的關係所以要加。
        res = UserSerializer(instance=pg_res, many=True, context={'request': request})
        # return Response(res.data)
        return pg_obj.get_paginated_response(res.data)

    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        if action == 'login':
            u_name = request.data.get('u_name')
            u_password = request.data.get('u_password')
            try:
                user = UserModel.objects.get(u_name=u_name)
                if user.u_password != u_password:
                    raise exceptions.AuthenticationFailed
                token = uuid.uuid4().hex
                cache.set(token, user.id, timeout=60 * 60)
                data = {
                    'msg': 'login success',
                    'status': 200,
                    'token': token,
                }
                return Response(data)

            except UserModel.DoesNotExist:
                raise exceptions.NotFound
        elif action == 'register':
            return self.create(request, *args, **kwargs)
        raise exceptions.ParseError


class UserAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = (LoginAuthentications,)
    permission_classes = (RequireLoginPermission,)

    # settings.py 可以全局添加 throttle。
    # throttle_classes = (UserThrottle, )
    # 下面這個是文檔 ScopedRateThrottle 用的，在影片153 最後有講一下，但沒實際操作。
    # throttle_classes = "10/m"

    def get(self, request, *args, **kwargs):
        # if instance.id != request.user.id:
        #     raise exceptions.AuthenticationFailed
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # 跟路徑參數比對，不用跟資料庫訪問
        if kwargs.get('pk') != str(request.user.id):
            raise exceptions.AuthenticationFailed
        instance = self.get_object()
        # 資料庫比對
        # if instance.id != request.user.id:
        #     raise exceptions.AuthenticationFailed
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AddressAPIView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    authentication_classes = (LoginAuthentications,)
    permission_classes = (RequireLoginPermission,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = request.user
        a_id = serializer.data.get('id')
        address = Address.objects.get(pk=a_id)
        # 關聯綁定下面這個也可以，只是給的東西要是 object，一直以來我都是指定給 ID。
        # address.a_user = user
        address.a_user_id = user.id
        address.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        # 篩選搜尋
        queryset = self.filter_queryset(self.queryset.filter(a_user=request.user))
        # 拿全部
        # queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TestAPIView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = SuperSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer