from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType


def home(request):
    main_wheels = MainWheel.objects.all()
    main_navs = MainNav.objects.all()
    main_mustbuys = MainMustBuy.objects.all()
    main_shop_0_1 = MainShop.objects.all()[0:1]
    main_shop_1_3 = MainShop.objects.all()[1:3]
    main_shop_3_7 = MainShop.objects.all()[3:7]
    main_shop_7_11 = MainShop.objects.all()[7:11]
    main_shows = MainShow.objects.all()
    data = {
        'title': '首頁',
        'main_wheels': main_wheels,
        'main_navs': main_navs,
        'main_mustbuys': main_mustbuys,
        'main_shop_0_1': main_shop_0_1,
        'main_shop_1_3': main_shop_1_3,
        'main_shop_3_7': main_shop_3_7,
        'main_shop_7_11': main_shop_7_11,
        'main_shows': main_shows,
    }
    return render(request, 'main/home.html', context=data)


def market(request):
    foodtypes = FoodType.objects.all()

    data = {
        'title': '超市',
    }
    return render(request, 'main/market.html')


def cart(request):
    return render(request, 'main/cart.html')


def mine(request):
    return render(request, 'main/mine.html')
