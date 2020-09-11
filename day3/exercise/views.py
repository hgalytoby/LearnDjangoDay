from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
# Create your views here.
from exercise.models import Student, Grade


def add_student(request, grade):
    data = request.GET
    grade_data = Grade.objects.get(g_name=grade)
    student_data = Student()
    student_data.s_name = data['student']
    student_data.s_grade_id = grade_data.id
    student_data.save()
    # return HttpResponseRedirect(reverse('exercise:get_student_list', kwargs={'grade': grade}))
    return redirect(reverse('exercise:get_student_list', kwargs={'grade': grade}))


def del_student(request):
    data = request.GET
    grade_id = Grade.objects.get(g_name=data['grade']).id
    Student.objects.filter(s_name=data['student']).filter(s_grade=grade_id).delete()
    return redirect(reverse('exercise:get_student_list', kwargs={'grade': data['grade']}))


def exercise(request):
    return render(request, 'exercise_get_grades.html', {'grade_data': Grade.objects.all()})


def get_student_list(request, grade):
    content = {
        'student_data': Grade.objects.get(g_name=grade).student_set.all().order_by('s_name'),
        'grade': grade,
        'url': request.path,
    }
    return render(request, 'exercise_get_students.html', context=content)


def have_request(request):
    # print('headers', request.headers)
    # print('user', request.user)
    # print('COOKIES', request.COOKIES)
    # print('session', request.session)
    # print('method', request.method)
    # print('META', request.META)
    # print('body', request.body)
    # print('get_host', request.get_host())
    # print('path', request.path)
    url = 'http://127.0.0.1:8000/exercise/have_request/?hobby=sleep&hobby=codeing'
    # print('GET', request.GET)
    # print(request.GET['hobby'])
    # print(request.GET.get('hobby'))
    # print(request.GET.getlist('hobby'))
    # print('POST', request.POST)
    # for i in request.META:
    #     print(i, request.META[i])
    print(request.META['REMOTE_ADDR'])
    return HttpResponse('read request')


def post_index(request):
    return render(request, 'exercise_post.html', {})


def post_data(request):
    print(request.POST.get('username'))
    # return render(request, 'exercise_post.html', {})
    return HttpResponse(request.POST.get('username'))
