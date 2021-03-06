from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app.models import Game
from app.serializers import GameSerializer


class GamesView(ListCreateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameView(RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class ReadGamesView(ListAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class ReadGameView(RetrieveAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameModelViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
