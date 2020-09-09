from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from app.models import Student


def hello(request):
    return HttpResponse('hello')


def index(request):
    temp = loader.get_template('index.html')
    content = temp.render()
    return HttpResponse(content)


def get_students(request):
    students = Student.objects.all().filter(s_name='hello')
    students = Student.objects.all()
    hobby_dict = {
        'hobby': 'coding',
        'time': 'year',
    }
    data = {
        'students': students,
        'hobby_dict': hobby_dict,
        'count': 5,
    }

    return render(request, 'get_students.html', context=data)