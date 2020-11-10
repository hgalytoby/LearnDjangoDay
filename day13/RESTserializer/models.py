from django.db import models


# Create your models here.

class Person(models.Model):
    p_name = models.CharField(max_length=32)
    p_age = models.IntegerField(default=1)
    p_sex = models.BooleanField(default=False)


class Student(models.Model):
    s_name = models.CharField(max_length=32)
    s_age = models.IntegerField(default=1)
