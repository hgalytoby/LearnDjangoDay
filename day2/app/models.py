from django.db import models


# Create your models here.

class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True, db_column='name')
    p_age = models.IntegerField(default=1, db_column='age')
    p_sex = models.BooleanField(default=False, db_column='sex')
    p_hobby = models.CharField(max_length=32, null=True, blank=True)

    # objects = models.Manager()
    @classmethod
    def create(cls, p_name='EE', p_age=27, p_sex=False, p_hobby='sex'):
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex, p_hobby=p_hobby)

    class Meta:
        db_table = 'People'
