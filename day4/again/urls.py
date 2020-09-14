from django.urls import path, include

from again import views

app_name = 'again'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('mine/', views.mine, name='mine'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('student_login/', views.student_login, name='student_login'),
    path('student_mine/', views.student_mine, name='student_mine'),
]
