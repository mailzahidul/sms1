from django.shortcuts import render, redirect
from .forms import StudentInfoForm


def createStudent(request):
    forms = StudentInfoForm()
    if request.method == 'POST':
        forms = StudentInfoForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    context = {'forms': forms}
    return render(request, 'student/createStudent.html', context)
