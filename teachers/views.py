from django.shortcuts import render, redirect
# from .forms import TeacherCreateForms
from .forms import TeacherCreateF
from .models import CreateTeacher


# Create your views here.
# def createTeacher(request):
#     forms = TeacherCreateForms()
#     if request.method == 'POST':
#         forms = TeacherCreateForms(request.POST)
#         if forms.is_valid():
#             t_name = forms.cleaned_data['name']
#             t_fname = forms.cleaned_data['father_name']
#             t_mname = forms.cleaned_data['mother_name']
#             t_email = forms.cleaned_data['email']
#             t_department = forms.cleaned_data['department']
#             t_contact = forms.cleaned_data['contact']
#
#             try:
#                 CreateTeacher.objects.create(
#                     name=t_name,
#                     father_name=t_fname,
#                     mother_name=t_mname,
#                     email=t_email,
#                     department=t_department,
#                     contact=t_contact
#                 )
#             except Exception as err:
#                 print(err)
#             return redirect('home')
#         print(forms)
#     context = {'forms': forms}
#     return render(request, 'teacher/createTeachers.html', context)

def createTeacher(request):
    forms = TeacherCreateF()
    if request.method == 'POST':
        forms = TeacherCreateF(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('home')
    context = {'forms': forms}
    return render(request, 'teacher/createTeachers.html', context)


def teacherList(request):
    tech_obj = CreateTeacher.objects.all()
    context = {'list': tech_obj}
    return render(request, 'teacher/teacherList.html', context)
