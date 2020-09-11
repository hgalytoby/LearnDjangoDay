from django.urls import path, include
from app import views

app_name = 'app'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('get_ticket/', views.get_ticket, name='get_ticket'),
    path('get_info/', views.get_info, name='get_info'),
]
