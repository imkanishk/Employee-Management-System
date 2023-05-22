from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')

def index(request):
    return render(request,'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetails.objects.create(user = user, empcode=ec)
            EmployeeExperience.objects.create(user = user)
            EmployeeEducation.objects.create(user = user)

            error="no"
        except:
            error="yes"
   
    return render(request,'registration.html',locals())

def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = 'no'
        else:
            error = 'yes'
    return render(request,'emp_login.html',locals())

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetails.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        desig = request.POST['designation']
        contact = request.POST['contact']
        doj = request.POST['doj']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = desig
        employee.contact = contact
        employee.gender = gender

        if doj:
            employee.doj = doj

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error="yes"
   
    return render(request,'profile.html',locals())

def Logout(request):
    logout(request)
    return redirect('emp_login')

def admin_login(request):
    return render(request,'admin_login.html')

def admin_login(request):
    return render(request,'admin_login.html')

def myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    return render(request,'myexperience.html',locals())

def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1_name = request.POST['company1_name']
        company1_desig = request.POST['company1_desig']
        company1_duration = request.POST['company1_duration']

        company2_name = request.POST['company2_name']
        company2_desig = request.POST['company2_desig']
        company2_duration = request.POST['company2_duration']

        company3_name = request.POST['company3_name']
        company3_desig = request.POST['company3_desig']
        company3_duration = request.POST['company3_duration']

        experience.company1_name  = company1_name
        experience.company1_desig  = company1_desig
        experience.company1_duration  = company1_duration
        experience.company2_name  = company2_name
        experience.company2_desig  = company2_desig
        experience.company2_duration  = company2_duration
        experience.company3_name  = company3_name
        experience.company3_desig  = company3_desig
        experience.company3_duration  = company3_duration


        try:
            experience.save()
            error = "no"
        except:
            error="yes"
   
    return render(request,'edit_experience.html',locals())

def myeducations(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    return render(request,'myeducations.html',locals())

def edit_myeducations(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        pg = request.POST['pg']
        yop_pg = request.POST['yop_pg']

        ug = request.POST['ug']
        yop_ug = request.POST['yop_ug']

        class_XII = request.POST['class_XII']
        yop_class_XII = request.POST['yop_class_XII']
        
        class_X = request.POST['class_X']
        yop_class_X = request.POST['yop_class_X']

        education.pg = pg
        education.yop_pg = yop_pg
        education.ug = ug
        education.yop_ug = yop_ug
        education.class_XII = class_XII
        education.yop_class_XII = yop_class_XII
        education.class_X = class_X
        education.yop_class_X = yop_class_X



        try:
            education.save()
            error = "no"
        except:
            error="yes"
   
    return render(request,'edit_myeducations.html',locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['current_password']
        n = request.POST['new_password'] 
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'change_password.html',locals())

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = "yes"
    return render(request,'admin_login.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def change_password_admin(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['current_password']
        n = request.POST['new_password'] 
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'change_password_admin.html',locals())

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetails.objects.all
    return render(request,'all_employee.html',locals())


def edit_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = User.objects.get(id=pid)
    employee = EmployeeDetails.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        desig = request.POST['designation']
        contact = request.POST['contact']
        doj = request.POST['doj']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = desig
        employee.contact = contact
        employee.gender = gender

        if doj:
            employee.doj = doj

        try:
            employee.save()
            error = "no"
        except:
            error="yes"
   
    return render(request,'edit_profile.html',locals())