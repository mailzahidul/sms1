from django.shortcuts import render


def createStudent(request):
    return render(request, 'student/createStudent.html')
