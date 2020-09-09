from django.urls import path
import multiprocessing
from dudulu import views

urlpatterns = [
    path('index/', views.index),
    path('get_class/', views.get_class),
    path('get_students/', views.get_students)
]