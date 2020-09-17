from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('news/', views.news, name='news'),
    path('many_cache/', views.many_cache, name='many_cache'),
    path('decorator_cache/', views.decorator_cache, name='decorator_cache'),
]
