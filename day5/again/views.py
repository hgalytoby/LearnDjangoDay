from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from again.models import Person, IDCard, Customer, Goods, Cat, Dog


def hello(request):
    return HttpResponse('hello')


def add_person(request):
    user_name = request.GET.get('username')
    person = Person()
    person.p_name = user_name
    person.save()
    return HttpResponse(f'User Name:{person.p_name} ID:{person.id}')


def add_idcard(request):
    id_num = request.GET.get('idnum')
    id_card = IDCard()
    id_card.id_num = id_num
    id_card.save()
    return HttpResponse(f'IDCard:{id_card.id_num} ID:{id_card.id}')


def bind_card(request):
    person = Person.objects.last()
    id_card = IDCard.objects.last()
    id_card.id_person = person
    id_card.save()
    return HttpResponse('綁定成功')


def remove_person(request):
    person = Person.objects.last()
    person.delete()
    return HttpResponse('Person remove ok')


def remove_idcard(request):
    id_card = IDCard.objects.last()
    id_card.delete()
    return HttpResponse('idcard remove ok')


def get_person(request):
    id_card = IDCard.objects.last()
    person = id_card.id_person
    return HttpResponse(f'{person.p_name}')


def get_idcard(request):
    person = Person.objects.last()

    return HttpResponse(f'{person.id} {person.p_name} {person.idcard.id_num} {person.idcard.id_person_id}')


def add_customer(request):
    c_name = request.GET.get('cname')
    customer = Customer()
    customer.c_name = c_name
    customer.save()
    return HttpResponse(f'add customer ok {customer.id}')


def add_goods(request):
    g_name = request.GET.get('gname')
    goods = Goods()
    goods.g_name = g_name
    goods.save()
    return HttpResponse(f'add goods ok {goods.id}')


def add_to_cart(request):
    customer = Customer.objects.last()
    goods = Goods.objects.last()
    goods.g_customer.add(customer)
    # goods.g_customer.remove(customer)
    # customer.goods_set.add(goods)
    # customer.goods_set.remove(goods)
    return HttpResponse(f'add to cart')


def get_good_list(request, c_id):
    customer = Customer.objects.get(pk=c_id)
    good_list = customer.goods_set.all()
    return render(request, 'goods_list.html', {'good_list': good_list})


def add_cat(request):
    cat = Cat.objects.all()
    num = cat.count()
    cat.create(a_name=f'cat{num}', c_eat='bear')
    return HttpResponse('cat ok')


def add_dog(request):
    dog = Dog.objects.all()
    num = dog.count()
    dog.create(a_name=f'dog{num}')
    return HttpResponse('dog ok')
