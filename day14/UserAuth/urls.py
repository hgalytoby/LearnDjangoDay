from django.urls import path

from UserAuth import views

app_name = 'ua'
urlpatterns =[
    path('users/', views.UsersAPIView.as_view(), name='users'),
    path('users/<str:pk>/', views.UserAPIView.as_view(), name='users-detail')
]