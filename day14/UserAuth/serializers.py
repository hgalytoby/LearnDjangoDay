from rest_framework import serializers

from UserAuth.models import UserModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ua:users-detail')

    class Meta:
        model = UserModel
        fields = ('url', 'id', 'u_name', 'is_super')
