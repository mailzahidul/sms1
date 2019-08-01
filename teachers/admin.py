from django.contrib import admin
from .models import CreateTeacher


# Register your models here.

class TeacherInfo(admin.ModelAdmin):
    list_display = ('name', 'email','contact', 'department')
    ordering = ('name',)
    search_fields = ('name', 'email')


admin.site.register(CreateTeacher, TeacherInfo)
