from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from CBV.models import Book


class HelloCBV(View):
    def get(self, request):
        return HttpResponse('hello get')

    def post(self, request):
        return HttpResponse('hello post')

    def put(self, request):
        return HttpResponse('hello put')


class BooksCBV(View):
    def get(self, request):
        book = Book.objects.all()
        book_list = list()
        for i in book:
            book_list.append(i.to_dict())
        data = {
            'status': 200,
            'msg': 'add_success',
            'data': book_list,
        }
        return JsonResponse(data)

    def post(self, request):
        b_name = request.POST.get('b_name')
        b_price = request.POST.get('b_price')
        book = Book()
        book.b_name = b_name
        book.b_price = b_price
        book.save()

        data = {
            'status': 201,
            'msg': 'add_success',
            'data': book.to_dict(),
        }
        return JsonResponse(data=data, status=data['status'])


class BookCBV(View):
    def get(self, request, book_id):
        book_obj = Book.objects.get(pk=book_id)
        data = {
            'status': 200,
            'msg': 'ok',
            'data': book_obj.to_dict()
        }
        return JsonResponse(data)

    def post(self, request, book_id):
        book_obj = Book.objects.get(pk=book_id)
        book_obj.delete()
        data = {
            'status': 204,
            'msg': 'delete success',
            # 'data': {}
        }
        return JsonResponse(data=data, status=data['status'])
