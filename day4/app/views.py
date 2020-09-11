from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def hello(request):
    response = HttpResponse()
    # response.content = 'hello, django'
    # response.status_code = 404
    response.write('用這個記得要用flush')
    response.flush()
    return response


def get_ticket(request):
    url = reverse('app:hello')
    # return HttpResponseRedirect(url)
    return redirect(url)


def get_info(request):
    return JsonResponse({'info': 'get ok'})
