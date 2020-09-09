from django.contrib import admin
from django.urls import path

from new import views

urlpatterns = {
    path('get_user/', views.get_user),
    path('get_users/', views.get_users),
    path('get_order/', views.get_order),
    path('get_grades/', views.get_grades),
    path('get_customer_max/', views.get_customer_max),
    path('get_company/', views.get_company),
    path('get_animal/', views.get_animal),
}