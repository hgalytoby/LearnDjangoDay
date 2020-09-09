from django.urls import path
from app_again import views

urlpatterns = [
    path('again/', views.again),
    path('add_student/', views.add_student),
    path('get_students/', views.get_students),
    path('del_students/', views.del_students),
    path('update_students/', views.update_students)
]