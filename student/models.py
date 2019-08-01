from django.db import models


# Create your models here.

class ShiftInfo(models.Model):
    shift = models.CharField(max_length=20)
    section = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s' % (self.shift, self.section)


class ClassInfo(models.Model):
    class_name = models.CharField(max_length=20)

    def __str__(self):
        return self.class_name


class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    class_name = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    roll = models.IntegerField()
    email = models.EmailField()
    contact_1 = models.IntegerField()
    contact_2 = models.IntegerField()
    shift = models.ForeignKey(ShiftInfo, on_delete=models.CASCADE)
    photo = models.ImageField()
    address = models.TextField()

    def __str__(self):
        return self.name
