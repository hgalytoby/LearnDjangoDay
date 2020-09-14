import time
import random
import hashlib
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError, ConnectionDoesNotExist
# Create your views here.
from django.urls import reverse

from again.models import Student


def hello(request):
    return HttpResponse('again hello')


def login(request):
    if request.method == 'GET':
        return render(request, 'again_login.html')
    elif request.method == 'POST':
        user_name = request.POST.get('username')
        print('in', user_name)
        request.session['username'] = user_name
        return redirect('again:mine')


def mine(request):
    username = request.session.get('username')
    return render(request, 'again_mine.html', context={'username': username})


def logout(request):
    response = redirect(reverse('again:mine'))
    # del request.session['username']
    # response.delete_cookie('sessionid')
    # Session Cookie 一起刪除
    request.session.flush()
    return response


def register(request):
    if request.method == 'GET':
        return render(request, 'again_register.html')
    elif request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            student = Student()
            student.s_name = user_name
            student.s_password = password
            student.save()
        except IntegrityError as error:
            print('重複名')
            return redirect(reverse('again:register'))
        return HttpResponse('ok')


def student_login(request):
    if request.method == 'GET':
        return render(request, 'student_login.html')
    elif request.method == 'POST':
        print(request.POST)
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        student = Student.objects.filter(s_name=user_name).filter(s_password=password)
        print(user_name, password)
        if student.exists():
            ip = request.META.get('REMOTE_ADDR')
            token = generate_token(ip=ip, user_name=user_name)
            student = student.first()
            student.s_token = token
            student.save()
            # response = redirect(reverse('again:student_mine'))
            # response.set_cookie('token', token)
            # return response
            data = {
                'status': 200,
                'msg': 'login ok',
                'token': token,
            }
            return JsonResponse(data=data)
        # return redirect(reverse('again:student_login'))
        data = {
            'status': 800,
            'msg': 'login error',
        }
        return JsonResponse(data=data)


def generate_token(ip, user_name):
    c_time = str(time.time())
    c_random = str(random.random())
    return hashlib.new('md5', (ip + c_time + c_random + user_name).encode('utf-8')).hexdigest()


def student_mine(request):
    # token = request.COOKIES.get('token')
    token = request.GET.get('token')
    try:
        student = Student.objects.get(s_token=token)
        # return HttpResponse(f'用戶名:{student.s_name} 密碼:{student.s_password}')
        data = {
            'status': 200,
            'msg': 'login ok',
            'data': {
                'student': student.s_name,
                'password': student.s_password
            },
        }
        return JsonResponse(data=data)
    except Student.DoesNotExist:
        return redirect(reverse('again:student_login'))
