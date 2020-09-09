from django.test import TestCase
from next.models import Grade, Student
import random

# Create your tests here.

print(random.randint(1, 4))
for i in range(20):
    student = Student()
    student.s_name = f'小火苗{i}'
    student.s_grade_id = random.randint(1, 4)
    student.save()
