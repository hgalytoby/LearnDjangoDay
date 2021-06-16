from django.contrib.auth.models import User, Group
from rest_framework import serializers

from App.models import UserModel, Address, Test


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='app:address-detail')
    a_user = serializers.HyperlinkedIdentityField(view_name='app:users-detail')

    class Meta:
        model = Address
        fields = ('url', 'id', 'a_address', 'a_user_id', 'a_user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='app:users-detail')
    address_set = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('url', 'id', 'u_name', 'u_password', 'address_set')


class TestSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='app:test-detail')
    t_owner = serializers.HyperlinkedIdentityField(view_name='app:users-detail')

    class Meta:
        model = Test
        fields = ('url', 'id', 't_name', 't_test', 't_owner', 't_owner_id')


class SuperSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='app:users-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
