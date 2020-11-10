from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from App.models import Book


class HelloView(View):
    def get(self, request):
        return render(request, 'hello.html')


class HelloTemplateView(TemplateView):
    template_name = 'hello.html'


class HelloListView(ListView):
    template_name = 'BookList.html'
    model = Book


class HelloDetailView(DetailView):

    # template_name = 'Book.html' # 不指定也行 根據 App名字在 template 資料夾下創App名字, html名字要是 model 名字(小寫) + _detail.html

    # 兩種 ORM 拿取都行
    model = Book
    # queryset = Book.objects.all()

