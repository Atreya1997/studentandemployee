from django.db import models

# Create your models here.
class Student(models.Model):
    Stu_name = models.CharField(max_length=100)
    age = models.IntegerField(default=100)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField(default=100)
    def __str__(self):
        return self.Stu_name

class Employee(models.Model):
    Emp_name = models.OneToOneField(Student, on_delete=models.CASCADE)
    Emp_No   = models.IntegerField(default=100)
    Dept_no  = models.IntegerField(default=100)
    Salary = models.IntegerField()   
    