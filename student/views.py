from django.shortcuts import render, redirect
from .forms import StudentInfoForm
from .models import StudentInfo


def createStudent(request):
    forms = StudentInfoForm()
    if request.method == 'POST':
        forms = StudentInfoForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    context = {'forms': forms}
    return render(request, 'student/createStudent.html', context)


def studentlist(request):
    stu_list = StudentInfo.objects.all()
    return render(request, 'student/studentList.html', {'stu_list': stu_list})


def classInfo(request, class_name):
    stu_list = StudentInfo.objects.filter(class_name__class_name=class_name)
    return render(request, 'student/classStudents.html', {'list': stu_list})
