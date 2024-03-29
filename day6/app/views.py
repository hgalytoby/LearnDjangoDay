from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.core.cache import cache, caches
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
import time
import random

# Create your views here.
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from app.models import Student
from utils import get_verify_code, get_color


def hello(request):
    return HttpResponse('Hello')


# # 單裝飾器 and 單資料庫
# @cache_page(30)
def news(request):
    result = cache.get('news')
    if result:
        return HttpResponse(result)
    news_list = list()
    for i in range(20):
        news_list.append(f'新聞{i}')
    time.sleep(2)
    data = {
        'news_list': news_list
    }
    response = render(request, 'news.html', context=data)
    cache.set('news', response.content, timeout=120)
    return response


# # 多選擇資料庫
def many_cache(request):
    # cache = caches['default']
    # cache = caches['redis_host']
    cache = caches['redis_drive']
    result = cache.get('many_cache_test')
    if result:
        return HttpResponse(result)
    time.sleep(2)
    response = HttpResponse('many_cache_test')
    print(response.content)
    cache.set('many_cache_test', response.content, timeout=120)
    return response


# # 多裝飾器
# @cache_page(30, cache='default')
# @cache_page(30, cache='redis_host')
@cache_page(30, cache='redis_drive')
def decorator_cache(request):
    data_list = list()
    for i in range(5):
        data_list.append(f'decorator_cache {i}')
    time.sleep(2)
    return render(request, 'decorator_cache.html', context={'data_list': data_list})


def ip(request):
    return HttpResponse('ip')


def get_prize(request):
    if random.randrange(100) > 80:
        return HttpResponse('bingo')
    return HttpResponse('bye')


def get_ticket(request):
    if random.randrange(100) > 10:
        return HttpResponse('還有剩餘的票')
    return None


def search(request):
    return HttpResponse('search ok')


def sequence_time(request):
    return HttpResponse('sequence_time ok')


def calc(request):
    a = 250
    b = 250
    result = (a + b) / 0
    return HttpResponse(result)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        if request.session['verify_code'] == request.POST.get('verify_code'):
            return HttpResponse('POST ok')
        return redirect(reverse('app:login'))


def add_students(request):
    count = Student.objects.count()
    for i in range(100):
        Student.objects.create(s_name=f'dudulu{i + count}', s_age=15 + i)
    return HttpResponse('add student ok')


def get_students(request):
    page = int(request.GET.get('page', default=1))
    per_page = int(request.GET.get('per_page', default=10))
    students = Student.objects.all()[(page - 1) * per_page:page * per_page]
    return render(request, 'get_students.html', context=locals())


def get_students_switch(request):
    page = request.GET.get('page', default=1)
    per_page = request.GET.get('per_page', default=10)
    students = Student.objects.all()
    paginator = Paginator(students, per_page)
    page_object = paginator.page(page)
    all_page = paginator.page_range
    if 0 < page_object.number - 5 and page_object.number + 5 < paginator.num_pages + 1:
        total_page = range(page_object.number - 5, page_object.number + 5)
    elif page_object.number + 5 > paginator.num_pages:
        total_page = range(paginator.num_pages - 9, paginator.num_pages + 1)
    else:
        total_page = range(1, 11)
    data = {'page_object': page_object,
            'page_range': total_page,
            'page_start': paginator.page_range.start,
            'page_end': paginator.page_range.stop - 1}
    return render(request, 'get_students_switch.html', context=data)


def get_code(request):
    # 初始化畫布
    image = Image.new(mode='RGB', size=(200, 100), color=get_color())
    # 初始化畫筆
    image_draw = ImageDraw.Draw(image, mode='RGB')
    # 字形 + 字體大小
    image_font = ImageFont.truetype(font=str(settings.FONT_PATH), size=50, encoding="unic")
    # 取得驗證碼
    verify_code = get_verify_code()
    # 存 session
    request.session['verify_code'] = verify_code
    # 畫字
    image_draw.text(xy=(10, 25), text=verify_code, font=image_font, fill=get_color())
    # 畫點 混淆
    for i in range(2500):
        image_draw.point(xy=(random.randrange(220), random.randrange(100)), fill=get_color())
    # 畫線
    # image_draw.line(xy=((100, 50), (50, 0)), fill=get_color(), width=7)

    fp = BytesIO()
    image.save(fp=fp, format='png')
    return HttpResponse(fp.getvalue(), content_type='image/png')


def signature_file(request):
    image = Image.new(mode='RGB', size=(660, 125), color=get_color())
    # image = Image.open(fp=r'image_path')
    image_draw = ImageDraw.Draw(image)
    image_font = ImageFont.truetype(font=str(settings.FONT_PATH), size=50)
    for k, v in request.META.items():
        print(k, v)
    # print(request.M)
    ip = f'你的 IP:{request.META["REMOTE_ADDR"]}'
    browser = request.META["HTTP_USER_AGENT"]
    # user_name = f'你的電腦名稱: {request.META["USERNAME"]}'
    # image_draw.text(xy=(250, 0), text='hello', font=image_font, fill=get_color())
    print(f'ip: {ip}')
    image_draw.text(xy=(100, 0), text=ip, font=image_font, fill=get_color())
    # image_draw.text(xy=(100, 50), text=user_name, font=image_font, fill=get_color())
    fp = BytesIO()
    image.save(fp=fp, format='png')
    return HttpResponse(fp.getvalue(), content_type='image/png')
