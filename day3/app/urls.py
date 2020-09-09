from django.urls import path, include
from app import views


urlpatterns = (
    path('hello/', views.hello),
    path('index/', views.index),
    path('get_students/', views.get_students)
)