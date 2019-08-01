from django.urls import path
from . import views

urlpatterns = [
    path('', views.createTeacher, name='create-teachers'),
    path('list/', views.teacherList, name='teacher-list')
]
