from django.contrib import admin
from .models import StudentInfo, ShiftInfo, ClassInfo
# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(ShiftInfo)
admin.site.register(ClassInfo)