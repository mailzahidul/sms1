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
    return render(request, 'student/classStudents.html', {'list': stu_list, 'class_n': class_name})


def studentDelete(request, student_id):
    std_obj = StudentInfo.objects.get(id=student_id)
    std_obj.delete()
    return redirect('student-list')


def studentView(request, student_id):
    std_obj = StudentInfo.objects.get(id=student_id)
    return render(request, 'student/studentView.html', {'student1': std_obj})


def studentEdit(request, student_id):
    std_obj = StudentInfo.objects.get(id=student_id)
    forms = StudentInfoForm(instance=std_obj)
    print("Request: ", forms)
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
        return redirect('student-list')
    return render(request, 'student/studentEdit.html', {'forms': forms})
