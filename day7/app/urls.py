from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('edit_blog/', views.edit_blog, name='edit_blog'),
]
