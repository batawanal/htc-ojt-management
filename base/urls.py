from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginPage, name='login'),


    # for teachers
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.adminHomePage, name='home'),
    path('company-list/', views.companyList, name="company-list"),
    path('student-list/', views.studentList, name="student-list"),
    path('account-list/', views.accountList, name="account-list"),
    path('student-schedule/', views.attendanceSched, name="attendance-schedule"),
    path('attendance-record/', views.studentAttendanceRecord, name="attendance-record"),

    path('create-account/', views.createUser, name="user-form"),
    path('create-company/', views.createCompany, name="company-form"),
    path('create-student/', views.createStudent, name="student-form"),
    path('create-attendanceSchedule/', views.createAttendance, name="attendance-scheduleform"),
    path('add-course/', views.createCourse, name="course-form"),

    path('update-account/<str:pk>', views.updateUser, name="update-account"),
    path('update-company/<str:pk>', views.updateCompany, name="update-company"),
    path('update-student/<str:pk>', views.updateStudent, name="update-student"),
    path('update-attendance/<str:pk>', views.updateAttendance, name="update-attendance"),

    path('delete-company/<str:pk>/', views.deleteCompany, name="delete-company"),
    path('delete-student/<str:pk>/', views.deleteStudent, name="delete-student"),
    path('delete-account/<str:pk>/', views.deleteUser, name="delete-account"),
    path('delete-attendance/<str:pk>/', views.deleteAttendance, name="delete-attendance"),


    # for students
    path('student-attendance/', views.studentAttendance, name="student-attendance"),

]


