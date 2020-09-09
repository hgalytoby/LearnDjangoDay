from django.urls import path, re_path, include
from app import views

urlpatterns = [
    path('hello/', views.hello),
    path('index/', views.index),
    path('get_students/', views.get_students),
    path('home/', views.home),
    path('home_main/', views.home_main),
    re_path(r'^hehe/', views.hehe),
    re_path(r'^hehehe/', views.hehehe),
]
