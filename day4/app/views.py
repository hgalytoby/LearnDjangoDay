import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def hello(request):
    response = HttpResponse()
    # response.content = 'hello, django'
    # response.status_code = 404
    response.write('用這個記得要用flush')
    response.flush()
    return response


def get_ticket(request):
    url = reverse('app:hello')
    # return HttpResponseRedirect(url)
    return redirect(url)


def get_info(request):
    return JsonResponse({'info': 'get ok'})


def set_cookie(request):
    response = HttpResponse('設定 Cookie')
    response.set_cookie('user', 'dudulu')
    response.set_cookie('pass', '123')
    return response


def get_cookie(request):
    cookies = request.COOKIES
    # print(json.dumps(cookies))
    return HttpResponse(json.dumps(cookies))


def login(request):
    print('in')
    return render(request, 'login.html')


def do_login(request):
    user_name = request.POST.get('user_name')
    # response = HttpResponse('登入成功')
    response = redirect(reverse('app:mine'))
    # 普通
    # response.set_cookie(key='user_name', value=user_name, max_age=600)
    # 普通 存中文
    response.set_cookie(key='user_name', value=json.dumps(user_name), max_age=600)
    # 加密
    # response.set_signed_cookie('content', user_name, 'dudulu')
    return response
    # return redirect(reverse('app:mine'))


def mine(request):
    try:
        # 普通
        # user_name = request.COOKIES.get('user_name')
        # 普通 存中文
        user_name = json.loads(request.COOKIES.get('user_name'))
        # 加密
        # user_name = request.get_signed_cookie('content', salt='dudulu')
        if user_name:
            # return HttpResponse(user_name)
            return render(request, 'mine.html', context={'user_name': user_name})
    except (KeyError, TypeError):
        print('取得 Cookies 失敗')
    return redirect(reverse('app:login'))


def logout(request):
    response = redirect(reverse('app:login'))
    # 普通
    response.delete_cookie('user_name')
    # 加密
    # response.delete_cookie('content')

    return response
