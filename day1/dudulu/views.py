from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from dudulu.models import Student, Grade


def index(request):
    dudulu_index = loader.get_template('index.html')
    result = dudulu_index.render(context={'name': 'dudulu'})
    print(result)
    # return render(request, 'index.html')
    return HttpResponse(result)


def get_class(request):
    students = Student.objects.get(pk=4)
    student = students.s_grade
    return HttpResponse(student.g_name)


def get_students(request):
    grade = Grade.objects.get(pk=2)
    students = grade.student_set.all()
    return render(request, 'students_list.html', {'students': students})
