from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createStudent, name='create-student'),
    path('list/', views.studentlist, name='student-list'),
    path('class/<class_name>', views.classInfo, name='class-name'),
    path('edit/<student_id>', views.studentEdit, name='student-edit'),
    path('delete/<student_id>', views.studentDelete, name='student-delete'),
    path('view/<student_id>', views.studentView, name='student-view'),
]