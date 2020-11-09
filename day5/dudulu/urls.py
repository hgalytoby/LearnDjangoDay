from django.urls import path

from dudulu import views

app_name = 'dudulu'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('image_field/', views.image_field, name='image_field'),
    path('mine/', views.mine, name='mine'),
    path('update_icon/', views.update_icon, name='update_icon'),
]
