from django.db import models


# Create your models here.

class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_age = models.IntegerField(default=1)
    p_sex = models.BooleanField(default=False)


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)


class Book(models.Model):
    b_name = models.CharField(max_length=16)
    b_price = models.FloatField(default=1)
