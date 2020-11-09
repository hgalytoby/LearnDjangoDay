from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from dudulu.models import UserModel


def index(request):
    return render(request, 'index.html', context={'user': 'user'})


def upload_file(request):
    if request.method == 'GET':
        return render(request, 'upload_file.html')
    elif request.method == 'POST':
        print(request.FILES.get('icon'))
        icon = request.FILES.get('icon')
        print(icon)
        with open(f'./static/img/{icon}', 'wb') as files:
            for i in icon.chunks():
                files.write(i)
                files.flush()
        return HttpResponse('upload file ok')


def image_field(request):
    if request.method == 'GET':
        return render(request, 'image_field.html')
    elif request.method == 'POST':
        user_name = request.POST.get('username')
        icon = request.FILES.get('icon')
        user = UserModel()
        user.u_name = user_name
        user.u_icon = icon
        user.save()
        return HttpResponse(f'image_field ok {user.id}')


def mine(request):
    user_name = request.GET.get('user_name')
    user = UserModel.objects.get(u_name=user_name)
    icon_url = user.u_icon.url
    data = {
        'user_name': user_name,
        'icon_url': f'/static/upload/{icon_url}',
    }
    return render(request, 'mine.html', context=data)


def update_icon(request):
    if request.method == 'GET':
        return render(request, 'update_icon.html')
    elif request.method == 'POST':

        user_name = request.POST.get('username')
        icon = request.FILES.get('icon')
        user = UserModel.objects.get(u_name=user_name)
        print(user.u_icon)
        user.u_icon.delete()
        user.u_icon = icon
        user.save()
        return HttpResponse(f'image_field ok {user.id}')