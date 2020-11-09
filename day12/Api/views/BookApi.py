from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Api.models import Book


@csrf_exempt
def books(request):
    if request.method == 'GET':
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
    elif request.method == 'POST':
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


@csrf_exempt
def book(request, book_id):
    if request.method == 'GET':
        book_obj = Book.objects.get(pk=book_id)
        data = {
            'status': 200,
            'msg': 'ok',
            'data': book_obj.to_dict()
        }
    elif request.method == 'DELETE':
        book_obj = Book.objects.get(pk=book_id)
        book_obj.delete()
        data = {
            'status': 204,
            'msg': 'delete success',
            # 'data': {}
        }
    return JsonResponse(data=data, status=data['status'])
