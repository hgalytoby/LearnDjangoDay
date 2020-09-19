from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('news/', views.news, name='news'),
    path('many_cache/', views.many_cache, name='many_cache'),
    path('decorator_cache/', views.decorator_cache, name='decorator_cache'),
    path('ip/', views.ip, name='ip'),
    path('get_prize/', views.get_prize, name='get_prize'),
    path('get_ticket/', views.get_ticket, name='get_ticket'),
    path('search/', views.search, name='search'),
    path('sequence_time/', views.sequence_time, name='sequence_time'),
    path('calc/', views.calc, name='calc'),
    path('login/', views.login, name='login'),
    path('add_students/', views.add_students, name='add_students'),
    path('get_students/', views.get_students, name='get_students'),
    path('get_students_switch/', views.get_students_switch, name='get_students_switch'),
    path('get_code/', views.get_code, name='get_code'),
]
