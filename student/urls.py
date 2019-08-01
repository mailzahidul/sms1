from django.urls import path
from . import views

urlpatterns = [
    path('', views.createStudent, name='create-student'),
]