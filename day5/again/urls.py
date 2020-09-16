from django.urls import path
from again import views

app_name = 'again'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('add_person/', views.add_person, name='add_person'),
    path('add_idcard/', views.add_idcard, name='add_idcard'),
    path('bind_card/', views.bind_card, name='bind_card'),
    path('remove_person/', views.remove_person, name='remove_person'),
    path('remove_idcard/', views.remove_idcard, name='remove_idcard'),
    path('get_person/', views.get_person, name='get_person'),
    path('get_idcard/', views.get_idcard, name='get_idcard'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_goods/', views.add_goods, name='add_goods'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('get_good_list/<str:c_id>/', views.get_good_list, name='get_good_list'),
    path('add_cat/', views.add_cat, name='add_cat'),
    path('add_dog/', views.add_dog, name='add_dog'),
]
