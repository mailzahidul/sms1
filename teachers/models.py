from django.db import models
from department.models import DepartmentName


# Create your models here.
class CreateTeacher(models.Model):
    name = models.CharField(max_length=70)
    father_name = models.CharField(max_length=70)
    mother_name = models.CharField(max_length=70)
    photo = models.ImageField(upload_to='media/teacher')
    email = models.EmailField()
    department = models.ForeignKey(DepartmentName, on_delete=models.CASCADE)
    address = models.TextField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name
