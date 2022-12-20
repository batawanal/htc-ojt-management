from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from . models import Student, User, Company, Course, StudentAttendance, AttendanceSchedule
from . forms import UserForm, CompanyForm, StudentForm, CourseForm, AttendanceScheduleForm
from . decorators import unauthenticated_user, allowed_users, admin_only
import requests, json
# Create your views here.
@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User OR Password does not exist')

    return render(request, 'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')
    
@login_required
@allowed_users(allowed_roles=['student'])
def studentAttendance(request):
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        res = requests.get('http://ip-api.com/json/' + ip_data["ip"])
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        schedules =  AttendanceSchedule.objects.all()
        if request.user.is_authenticated:
            
            attendance = StudentAttendance(attender=request.user)
            attendance.save()
                
        context = {'schedules': schedules, 'data': location_data}
        return render(request, 'base/student-attendance.html', context) 

@login_required
@admin_only
def attendanceSched(request):
    schedules =  AttendanceSchedule.objects.all()
    context = {'schedules': schedules}

    return render(request, 'base/attendance-schedule.html', context)

@login_required
@admin_only
def createAttendance(request):
    form = AttendanceScheduleForm()
    if request.method == 'POST':
        form = AttendanceScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance-schedule')

    context = {'form': form}
    return render(request, 'base/attendance-scheduleform.html', context)

@login_required
@admin_only
def updateAttendance(request, pk):
    schedule =  AttendanceSchedule.objects.get(id=pk)
    form = AttendanceScheduleForm(instance=schedule)
    if request.method == 'POST':
        form = AttendanceScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('attendance-schedule')
            
    context = {'form': form}
    return render(request, 'base/attendance-scheduleform.html', context)

@login_required
@admin_only
def deleteAttendance(request, pk):
    schedule = AttendanceSchedule.objects.get(id=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('attendance-schedule')

    context = {'obj': schedule}
    return render(request, 'base/delete.html', context)

@login_required
@admin_only
def studentAttendanceRecord(request):
    records =  StudentAttendance.objects.all()
    context = {'records': records}
    return render(request, 'base/student-attendance-record.html', context)

@login_required
@admin_only
def adminHomePage(request):
    context = {}
    return render(request, 'base/admin-home.html', context)


@login_required
@admin_only
def companyList(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'base/company-list.html', context)

@login_required
@admin_only
def studentList(request):
    students = Student.objects.all()
    context = {'students': students}

    return render(request, 'base/student-list.html', context)

@login_required
@admin_only
def accountList(request):
    accounts = User.objects.all()
    context = {'accounts': accounts}

    return render(request, 'base/account-list.html', context)

@login_required
@admin_only
def createUser(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)

            return redirect('account-list')

    context = {'form': form}
    return render(request, 'base/user-form.html', context)

@login_required
@admin_only
def updateUser(request, pk):
    account =  User.objects.get(id=pk)
    form = UserForm(instance=account)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account-list')
    context = {'form': form}
    return render(request, 'base/user-form.html', context)

@login_required
@admin_only
def deleteUser(request, pk):
    account = User.objects.get(id=pk)

    if request.method == 'POST':
        account.delete()
        return redirect('account-list')

    context = {'obj': account}
    return render(request, 'base/delete.html', context)

@login_required
@admin_only
def createCompany(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company-list')

    context = {'form': form}
    return render(request, 'base/company-form.html', context)

@login_required
@admin_only
def updateCompany(request, pk):
    company =  Company.objects.get(id=pk)
    form = CompanyForm(instance=company)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company-list')
            
    context = {'form': form}
    return render(request, 'base/student-form.html', context)

@login_required
@admin_only
def deleteCompany(request, pk):
    company = Company.objects.get(id=pk)

    if request.method == 'POST':
        company.delete()
        return redirect('company-list')

    context = {'obj': company}
    return render(request, 'base/delete.html', context)

@login_required
@admin_only
def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')

    context = {'form': form}
    return render(request, 'base/student-form.html', context)

@login_required
@admin_only
def updateStudent(request, pk):
    student =  Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')

    context = {'form': form}
    return render(request, 'base/student-form.html', context)

@login_required
@admin_only
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student-list')

    context = {'obj': student}
    return render(request, 'base/delete.html', context)

@login_required
@admin_only
def createCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')

    context = {'form': form}
    return render(request, 'base/course-form.html', context)


