from django.db.models import Max, Avg, F, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from new.models import User, Order, Grade, Student, Customer, Company, Animal


def get_user(request):
    user_name = '小火苗'
    user_password = '123'
    data = User.objects.filter(u_name=user_name)
    # if data.count():
    if data.exists():
        data = data.first()
        if data.u_password == user_password:
            print('ok')
    else:
        print('out')
    return HttpResponse('get_user ok')


def get_users(request):
    data = User.objects.all()
    # data = User.objects.all()[1:3]
    lenght = data.count()
    result = data[0:lenght-2]
    for i in data:
        print(i.u_name)
    context = {
        'data': result
    }
    return render(request, 'get_users_list.html', context=context)


def get_order(request):
    data = Order.objects.filter(o_time__month=9)
    for i in data:
        print(i.o_time)
    return HttpResponse('get_order ok')


def get_grades(request):
    grades = Grade.objects.filter(student__s_name='小火苗4')
    students = Student.objects.filter(s_grade='1').order_by('-id')
    # students.order_by()
    for grade in grades:
        print(grade.g_name)
    for student in students:
        print(student.s_name)
    return HttpResponse('get_grades ok')


def get_customer_max(request):
    result = Customer.objects.aggregate(Max('c_cost'))
    result = Customer.objects.aggregate(Avg('c_cost'))
    customer = Customer.objects.filter(c_cost__isnull=True)
    for i in customer:
        print(i.c_name, i.c_cost)
    # print(customer)

    return HttpResponse('get_customer_max ok')


def get_company(request):
    companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num'))
    companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num') - 6)

    # companies = Company.objects.filter(c_boy_num__gt=5).filter(c_girl_num__gt=5)
    # companies = Company.objects.filter(Q(c_boy_num__gt=5) | Q(c_girl_num__gte=20))

    for i in companies:
        print(i.c_name)
    return HttpResponse('get_company ok')


def get_animal(request):
    animal = Animal.objects.all()
    animal = Animal.a_obj.all()
    for i in animal:
        print(i.a_name)
    # animal = Animal.a_obj.create_animal(a_name='tiger', is_delete=True)
    # animal.save()
    return HttpResponse('get_animal ok')
