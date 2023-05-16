from django.db import models

# Create your models here.
 

class Student(models.Model):
    Sname=models.CharField(max_length=20)
    Sage=models.IntegerField()
    Email=models.EmailField()
class Course(models.Model):
    coursename=models.CharField(max_length=20)