from django.urls import path

from app import views

urlpatterns = {
    path('add_persons/', views.add_persons),
    path('get_persons_list/', views.get_persons_list),
    path('get_person/', views.get_person)
}