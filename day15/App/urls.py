from django.urls import path
from rest_framework.routers import DefaultRouter

from App import views
from App.views import TestAPIView, UsersAPIView

app_name = 'app'

router = DefaultRouter()
router.register('tests', TestAPIView)
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    path('users/', views.UsersAPIView.as_view(), name='users'),
    path('users/<str:pk>/', views.UserAPIView.as_view(), name='users-detail'),
    path('address/', views.AddressAPIView.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    )),
    path('address/<str:pk>/', views.AddressAPIView.as_view(
        {
            'get': 'retrieve',
        }
    ), name='address-detail'),
    path('test/', views.TestAPIView.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    )),
    path('test/<str:pk>/', views.TestAPIView.as_view(
        {
            'get': 'retrieve',
        }
    ), name='test-detail'),
]
