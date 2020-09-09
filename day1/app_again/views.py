from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app_again.models import Student
import random


# Create your views here.


def again(request):
    return HttpResponse('again ok')


def add_student(request):
    student = Student()
    student.s_name = f'小火苗{random.randrange(1, 100)}'
    student.s_age = random.randrange(1, 100)
    student.save()
    return HttpResponse('add_student ok')


def get_students(request):
    students = Student.objects.all()
    return render(request, 'get_students.html', {'students': students})


def del_students(request):
    students = Student.objects.get(s_age=81)
    students.delete()
    return HttpResponse('del_students ok')


def update_students(request):
    students = Student.objects.get(s_age=92)
    # print(students.__dict__)
    students.s_name = '修改測試'
    students.save()
    return HttpResponse('update_student ok')