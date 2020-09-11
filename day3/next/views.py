import random

from django.http import HttpResponse
from django.shortcuts import render
from next.models import Grade, Student


# Create your views here.
def students(request):
    return HttpResponse('Get Students Success')


def student(request, s_id):
    students_grade = Student.objects.filter(s_grade_id=s_id)
    grade_students = Grade.objects.get(pk=s_id).student_set.all()
    return render(request, 'get_grade_student.html', context=locals())


def grades(request):
    return render(request, 'grades_list.html', context={'grades': Grade.objects.all()})


def get_time(request, h, m, s):
    return HttpResponse(f'Time {h} : {m} : {s}')


def getdate(request, year, month, day):
    return HttpResponse(f'date {year}/{month}/{day}')


def get_date(request, month, day, year):
    return HttpResponse(f'date {year}/{month}/{day}')


def learn(request):
    return HttpResponse('happy learn')
