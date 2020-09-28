from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods


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
    return redirect(reverse('axf:market_with_params', kwargs={'typeid': 104749, 'childcid': 0}))


def market_with_params(request, typeid, childcid):
    foodtypes = FoodType.objects.all()
    all_type = '0'
    if childcid == all_type:
        goods_list = Goods.objects.filter(categoryid=typeid)
    else:
        goods_list = Goods.objects.filter(categoryid=typeid, childcid=childcid)

    """
    全部分類:0#進口水果:103534#國產水果:103533
    切割 #
        [全部分類:0, 進口水果:103534, 國產水果:103533]
    切割 :
        [[全部分類,0], [進口水果, 103534], [國產水果, 103533]]]
    """

    foodtype_childnames = foodtypes.get(typeid=typeid).childtypenames
    foodtype_childname_list = list()
    for i in foodtype_childnames.split('#'):
        foodtype_childname_list.append(i.split(':'))
    data = {
        'title': '超市',
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'typeid': typeid,
        'foodtype_childname_list': foodtype_childname_list,
        'childcid': childcid,
    }
    return render(request, 'main/market.html', context=data)


def cart(request):
    return render(request, 'main/cart.html')


def mine(request):
    return render(request, 'main/mine.html')
