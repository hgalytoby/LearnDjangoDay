from django.urls import path, include
from app import views

app_name = 'axf'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('market_with_params/<int:typeid>/<str:childcid>/<str:order_rule>/', views.market_with_params,
         name='market_with_params'),
    path('cart/', views.cart, name='cart'),
    path('mine/', views.mine, name='mine'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('check_user/', views.check_user, name='check_user'),
    path('check_email/', views.check_email, name='check_email'),
]
