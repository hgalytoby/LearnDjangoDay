from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from UserAuth.models import UserModel
from UserAuth.serializers import UserSerializer
from project.settings import SUPER_USERS


class UsersAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def create(self, request, *args, **kwargs):
        u_name = request.data.get('u_name')
        if u_name in SUPER_USERS:
            print(dir(request.data))
            request.data.update({'is_super': True})

            u_id = request.data.get('id')
            user = UserModel.objects.get(pk=u_id)
            user.is_super = True
            user.save()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # data = serializer.data
        # u_name = data.get('u_name')
        # if u_name in SUPER_USERS:
        #     u_id = data.get('id')
        #     user = UserModel.objects.get(pk=u_id)
        #     user.is_super = True
        #     user.save()
        #     print('super')
        #     data.update({'is_super': True})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
