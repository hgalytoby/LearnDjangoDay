from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from six import BytesIO

from RESTserializer.models import Person, Student
from RESTserializer.serializers import PersonSerializer, StudentSerializer, BookSerializer


class PersonView(GenericAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get(self, request):
        person = Person.objects.all()
        # many 參數是指多個資料的意思。
        # 因為是.objects.all()。
        person_serializer = PersonSerializer(person, many=True)
        # 因為是 dict ，所以 safe 要設定成 False。
        # return JsonResponse(person_serializer.data, safe=False)
        return Response(data=person_serializer.data)

    def post(self, request):
        person_serializer = PersonSerializer(data=request.data)
        if request.data.get('id'):
            person_serializer.instance = Person.objects.get(pk=request.data.get('id'))
        else:
            person_serializer.fields.pop('id')
        if person_serializer.is_valid():
            person_serializer.save()
            # return JsonResponse(student_serializer.data)
            return Response(person_serializer.data)  # 這個也是 JsonResponse
        return JsonResponse(person_serializer.errors, status=400)
        # p_name = request.POST.get('p_name')
        # p_age = request.POST.get('p_age')
        # person = Person()
        # person.p_name = p_name
        # person.p_age = p_age
        # person.save()
        # person_serializer = PersonSerializer(person)
        # return JsonResponse(person_serializer.data)
        # return Response(person_serializer.data)


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
        以上是在 shell。
        student_ser = StudentSerializer(data=data)
        student_ser.is_valid()
        student_ser.save()

        """
        # 第一種
        # 繼承 View 不是 APIView。
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
            # return JsonResponse(student_serializer.data)
            return Response(student_serializer.data)  # 這個也是 JsonResponse
        return JsonResponse(student_serializer.errors, status=400)


# @api_view()  #  默認指允許GET 可點原始碼看!
@api_view(http_method_names=['GET', 'POST', ])  # 只允許列表內的狀態
def books(request):
    print(type(request))
    if request.method == 'GET':
        return Response(data={'msg': 'get ok'})
    elif request.method == 'POST':
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data)
        return Response(data={'msg': 'error'}, status=status.HTTP_400_BAD_REQUEST)
