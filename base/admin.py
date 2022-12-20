from django.contrib import admin
from . models import User, Student, Company, Course, AttendanceSchedule, StudentAttendance
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Course)
admin.site.register(StudentAttendance)
admin.site.register(AttendanceSchedule)
