from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_dean = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    company_assign = models.ForeignKey('Company', null=True ,on_delete=models.SET_NULL)
    course = models.ForeignKey('Course',  null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    
    def __str__(self):
        fullname = self.first_name + ' ' + self.last_name
        return fullname
 
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class StudentAttendance(models.Model):
    #date = models.ForeignKey(AttendanceSchedule)
    id = models.AutoField(primary_key=True)
    attender = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time =  models.DateTimeField(auto_now_add = True) 
    

    def __str__(self):
        return str(str(self.attender.username) + " " + str(self.date_time))[:-7]

class AttendanceSchedule(models.Model):
      date = models.DateField(auto_created=True)

      def __str__(self):
        return str(self.date)




