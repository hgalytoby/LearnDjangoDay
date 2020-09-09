from django.urls import path, re_path
from next import views

urlpatterns = [
    path('students/', views.students),
    re_path(r'^students/(\d+)/', views.student),
    path('grades/', views.grades),

]
