from django.urls import path, re_path
from next import views

app_name = 'next'
urlpatterns = [
    path('students/', views.students),
    # path('students/<str:s_id>/', views.student),
    # path('students/<int:s_id>/', views.student),
    re_path(r'^students/(\d+)/', views.student, name='get_grade_students'),
    re_path(r'^time/(\d+)/(\d+)/(\d+)/', views.get_time, name='time'),
    re_path(r'^getdate/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)', views.get_date),
    re_path(r'^get_date_arg/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)', views.getdate, name='date'),
    path('get_date/<str:year>/<str:month>/<str:day>/', views.get_date),
    path('grades/', views.grades),
    path('learn/', views.learn, name='happy_learn'),
]
