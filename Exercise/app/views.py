from django.contrib.auth.hashers import make_password, check_password

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
# Create your views here.
from django.urls import reverse

from app.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods, AXFUser
from app import views_helper
from project.settings import MEDIA_KEY_PREFIX


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
    return redirect(reverse('axf:market_with_params', kwargs={'typeid': 104749, 'childcid': 0, 'order_rule': 0}))


def market_with_params(request, typeid, childcid, order_rule):
    foodtypes = FoodType.objects.all()
    all_type = '0'
    order_mode = {'0': '全部類型',
                  '1': '價錢升序',
                  '2': '價錢降序',
                  '3': '銷量升序',
                  '4': '銷量降序', }
    if childcid == all_type:
        goods_list = Goods.objects.filter(categoryid=typeid)
    else:
        goods_list = Goods.objects.filter(categoryid=typeid, childcid=childcid)

    if order_mode[order_rule] == '全部類型':
        pass
    elif order_mode[order_rule] == '價錢升序':
        goods_list = goods_list.order_by('price')
    elif order_mode[order_rule] == '價錢降序':
        goods_list = goods_list.order_by('-price')
    elif order_mode[order_rule] == '銷量升序':
        goods_list = goods_list.order_by('productnum')
    elif order_mode[order_rule] == '銷量降序':
        goods_list = goods_list.order_by('-productnum')

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
        'order_rule': order_rule,
        'order_mode': order_mode,
    }
    return render(request, 'main/market.html', context=data)


def cart(request):
    return render(request, 'main/cart.html')


def mine(request):
    user_id = request.session.get('user_id')
    data = {
        'title': '個人中心',
        'is_login': False,
    }
    if user_id:
        user = AXFUser.objects.get(pk=user_id)
        data['username'] = user.u_user
        data['icon'] = MEDIA_KEY_PREFIX + user.u_icon.url
        print(data['icon'])
        data['is_login'] = True
    return render(request, 'main/mine.html', data)


def register(request):
    if request.method == 'GET':
        data = {
            'title': '註冊'
        }
        return render(request, 'user/register.html', context=data)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')
        user = AXFUser()
        user.u_user = username

        # 自製
        user.u_password = views_helper.hash_password(password)

        # django 內建
        user.u_password = make_password(password=password)

        user.u_email = email
        user.u_icon = icon
        user.save()
        return redirect(reverse('axf:login'))


def login(request):
    if request.method == 'GET':
        if request.session.get('user_id'):
            return HttpResponse('ok')
        data = {
            'title': '登入'
        }
        return render(request, 'user/login.html', context=data)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = AXFUser.objects.filter(u_user=username)
        if user.exists():
            user = user.first()
            check = check_password(password=password, encoded=user.u_password)
            if check:
                request.session['user_id'] = user.id
                return redirect(reverse('axf:mine'))
        return redirect(reverse('axf:login'))


def check_user(request):
    username = request.GET.get('username')
    user = AXFUser.objects.filter(u_user=username)
    user_exist = 901
    user_ok = 200
    data = {
        'status': user_ok,
        'msg': 'user can use',
    }
    if user.exists():
        data['status'] = user_exist
        data['msg'] = 'user already'
    return JsonResponse(data)


def check_email(request):
    email_type = {
        'ok': 200,
        'error': 902,
        'exists': 903,
    }
    data = {
        'status': email_type['ok'],
        'msg': 'email can use',
    }
    email = request.GET.get('email')
    try:
        validate_email(email)
    except ValidationError as e:
        data['status'] = email_type['error']
        data['msg'] = 'email error'
        return JsonResponse(data)
    email_db = AXFUser.objects.filter(u_email=email)
    if email_db.exists():
        data['status'] = email_type['exists']
        data['msg'] = 'email exists'
        return JsonResponse(data)
    return JsonResponse(data)


def logout(request):
    request.session.flush()

    return redirect(reverse('axf:mine'))



