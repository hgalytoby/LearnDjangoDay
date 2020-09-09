from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hello(request):
    return render(request, 'hello.html')


def home(request):
    return render(request, 'today.html')