from rest_framework import serializers

from app.models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='app:game-detail')

    class Meta:
        model = Game
        fields = ('url', 'id', 'g_name', 'g_price')
