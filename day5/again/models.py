from django.db import models


# Create your models here.

class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_sex = models.BooleanField(default=False)


class IDCard(models.Model):
    id_num = models.CharField(max_length=16, unique=True)
    # id_person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True, blank=True)
    # id_person = models.OneToOneField(Person, on_delete=models.PROTECT, null=True, blank=True)
    id_person = models.OneToOneField(Person, on_delete=models.SET_NULL, null=True, blank=True)
    # id_person = models.OneToOneField(Person, on_delete=models.SET_DEFAULT, default=7)
    # id_person = models.OneToOneField(Person, on_delete=models.SET(7), null=True, blank=True)


class Customer(models.Model):
    c_name = models.CharField(max_length=16)


class Goods(models.Model):
    g_name = models.CharField(max_length=16)
    g_customer = models.ManyToManyField(Customer)
