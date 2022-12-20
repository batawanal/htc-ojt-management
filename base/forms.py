
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from . models import Student, Company, User, Course, AttendanceSchedule


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_student']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class AttendanceScheduleForm(ModelForm):
    class Meta:
        model = AttendanceSchedule
        fields = '__all__'