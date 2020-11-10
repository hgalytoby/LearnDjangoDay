from django.contrib.auth.models import User, Group
from rest_framework import viewsets

# Create your views here.
from REST.models import Book
from REST.serializers import UserSerializers, GroupSerializers, BookSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
