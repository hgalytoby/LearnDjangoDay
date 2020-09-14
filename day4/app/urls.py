from django.urls import path, include
from app import views

app_name = 'app'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('get_ticket/', views.get_ticket, name='get_ticket'),
    path('get_info/', views.get_info, name='get_info'),
    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('get_cookie/', views.get_cookie, name='get_cookie'),
    path('login/', views.login, name='login'),
    path('do_login/', views.do_login, name='do_login'),
    path('mine/', views.mine, name='mine'),
    path('logout/', views.logout, name='logout'),
]
