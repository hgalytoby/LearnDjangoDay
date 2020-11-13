from django.urls import path
from rest_framework.routers import DefaultRouter

from app import views
from app.views import GameModelViewSet

app_name = 'app'

urlpatterns = [
    path('games/', views.GamesView.as_view()),
    path('games/<str:pk>/', views.GameView.as_view(), name='game-detail'),
]

router = DefaultRouter()

router.register('games', GameModelViewSet)
