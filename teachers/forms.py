from django import forms
from .models import CreateTeacher

# dept_choice = (
#     ('th', 'Mathematics'),
#     ('cse', 'Computer Science'),
#     ('eee', 'EEE'),
#     ('me', 'Mechanical'),
# )
#
#
# class TeacherCreateForms(forms.Form):
#     name = forms.CharField()
#     father_name = forms.CharField()
#     mother_name = forms.CharField()
#     email = forms.EmailField()
#     department = forms.ChoiceField()
#     contact = forms.IntegerField()


class TeacherCreateF(forms.ModelForm):
    class Meta:
        model = CreateTeacher
        fields = '__all__'
