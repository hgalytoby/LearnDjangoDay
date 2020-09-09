from django.http import HttpResponse
from django.shortcuts import render
import datetime
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
    # code = """
    #         <h1>努力中</h1>
    #         <script type="text/javascript">
    #             alert("網站被攻擊了!");
    #         </script>
    #         """
    code = """
            <h1>努力中</h1>
            <script type="text/javascript">
                
                var lis = document.getElementsByTagName("li")
                for (var i = 0; i < lis.length; i++) {
                    var li = lis[i]
                    li.innerHTML = "持續攻擊!";
                }
            </script>
           """
    data = {
        'students': students,
        'hobby_dict': hobby_dict,
        'count': 5,
        'today': datetime.datetime.today(),
        'code': code,
    }
    return render(request, 'get_students.html', context=data)


def home(request):
    content = {
        'title': '再來啊!',
    }
    return render(request, 'home.html', context=content)


def home_main(request):
    content = {
    }
    return render(request, 'home_main.html', context=content)


def hehehe(request):
    return HttpResponse('hehehe')


def hehe(request):
    return HttpResponse('hehe')
