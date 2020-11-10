from django.urls import path

from App import views

app_name = 'cbv'
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    # path('template/', views.HelloTemplateView.as_view(template_name='hello.html'), name='template'),
    path('template/', views.HelloTemplateView.as_view(), name='template'),
    path('listview/', views.HelloListView.as_view(), name='listview'),
    path('single/<str:pk>/', views.HelloDetailView.as_view(), name='single'),
]
