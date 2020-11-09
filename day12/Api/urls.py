from django.urls import path

from Api import views

app_name = 'api'

urlpatterns = [
    path('books/', views.books, name='books'),
    path('books/<str:book_id>/', views.book, name='book'),
]
