from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from six import BytesIO

from RESTserializer.models import Person, Student
from RESTserializer.serializers import PersonSerializer, StudentSerializer


class PersonView(View):
    def get(self, request):
        person = Person.objects.all()
        person_serializer = PersonSerializer(person, many=True)
        return JsonResponse(person_serializer.data, safe=False)

    def post(self, request):
        p_name = request.POST.get('p_name')
        p_age = request.POST.get('p_age')
        person = Person()
        person.p_name = p_name
        person.p_age = p_age
        person.save()
        person_serializer = PersonSerializer(person)
        return JsonResponse(person_serializer.data)


class StudentView(APIView):
    def post(self, request):
        """
        影片教學遇到的BUG。
        驗證 JSONParser python manage shell
        from RESTserializer.models import Student
        student = Student.objects.first()
        student
        from RESTserializer.serializers import StudentSerializer
        student_serializer = StudentSerializer(student)
        student_serializer.data
        from rest_framework.renderers import JSONRenderer
        content = JSONRenderer().render(student_serializer.data)
        content
        content.decode('utf-8')
        from django.utils.six import BytesIO   <- 新版本刪除了
        pip install six
        from six import BytesIO
        stream = BytesIO(content)
        stream
        from rest_framework.parsers import JSONParser
        data = JSONParser().parse(stream)
        data
        student_ser = StudentSerializer(data=data)
        student_ser.is_valid()
        student_ser.save()

        """
        # 第一種
        # s_name = request.POST.get('s_name')
        # s_age = request.POST.get('s_age')
        # student = Student()
        # student.s_name = s_name
        # student.s_age = s_age
        # student.save()
        # student_serializer = StudentSerializer(student)
        # return JsonResponse(student_serializer.data)

        # 第二種
        # print(request.GET) # POST時 也能取得GET的東西
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(student_serializer.errors, status=400)


