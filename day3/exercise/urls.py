from django.urls import path, re_path

from exercise import views

app_name = 'exercise'
urlpatterns = [
    path('grades/', views.exercise, name='exercise_grades'),
    path('grades/get_student_list/<str:grade>/', views.get_student_list, name='get_student_list'),
    path('grades/add_student/<str:grade>/', views.add_student, name='add_student'),
    path('grades/del_student/', views.del_student, name='del_student'),
    path('have_request/', views.have_request),
    path('post_index/', views.post_index, name='post_index'),
    path('post_data/', views.post_data, name='post_data'),
]
