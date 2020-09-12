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
    import json

    # print(json.dumps(cookies))
    return HttpResponse(json.dumps(cookies))


def login(request):
    return render(request, 'login.html')


def do_login(request):
    user_name = request.POST.get('user_name')
    response = HttpResponse('登入成功')
    # response.set_cookie(key='user_name', value=user_name, max_age=60)
    response.set_signed_cookie('content', user_name, 'dudulu')
    return response
    # return redirect(reverse('app:mine'))


def mine(request):
    # user_name = request.COOKIES.get('user_name')
    user_name = request.get_signed_cookie('coontent', salt='user_name')
    if user_name:
        return HttpResponse(user_name)
    return redirect(reverse('app:login'))
