from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createStudent, name='create-student'),
    path('list/', views.studentlist, name='student-list'),
    path('class/<class_name>', views.classInfo, name='class-name'),
]