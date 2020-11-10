from django.urls import path

from CBV import views

app_name = 'cbv'

urlpatterns = [
    path('hello/', views.HelloCBV.as_view(msg='msg hello'), name='hello'),
    path('books/', views.BooksCBV.as_view(), name='books'),
    path('books/<str:book_id>/', views.BookCBV.as_view(), name='book'),
]
