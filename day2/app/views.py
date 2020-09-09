import random

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import Person


def add_persons(request):
    # person = Person.objects
    # for i in range(10):
    #     num = random.randint(201, 400)
    #     person.create(p_age=num, p_sex=num % 2, p_name=f'官定E{num}')
        # person.p_age = num
        # person.p_name =
        # person.p_sex = num % 2
        # person.save()
    person = Person.create()
    person.save()

    return HttpResponse('add_persons ok')


def get_persons_list(request):
    # persons = Person.objects.filter(p_age__gt=18).filter(p_age__lt=80)
    # persons = Person.objects.exclude(p_age__lt=83).exclude(p_age__gt=150)
    persons = Person.objects.all().order_by('p_age')
    # persons = Person.objects.
    # persons = Person.objects.order_by('-p_age')
    # persons_values = persons.values()
    # print(persons_values)
    # for i in persons.values():
    #     print(i)
    context = {
        'persons': persons
    }
    return render(request, 'get_persons.html', context=context)


def get_person(request):
    persons = Person.objects.all().first()
    print(persons.p_name)
    persons = Person.objects.all().last()
    print(persons.p_name)
    return HttpResponse('get_person ok')