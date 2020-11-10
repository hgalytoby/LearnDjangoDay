from django.urls import path

from RESTserializer import views

app_name = 'ser'

urlpatterns =[
    path('persons/', views.PersonView.as_view(), name='persons'),
    path('students/', views.StudentView.as_view(), name='students'),
]

