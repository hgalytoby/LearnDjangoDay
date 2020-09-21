from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def market(request):
    return render(request, 'main/market.html')


def mine(request):
    return render(request, 'main/mine.html')


def cart(request):
    return render(request, 'main/cart.html')
