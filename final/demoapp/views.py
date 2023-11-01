from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Student

# Create your views here.
def demo(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        name=request.POST['username']
        passw=request.POST['password']
        cpass=request.POST['password1']
        if passw == cpass:
            if User.objects.filter(username=name).exists():
                messages.info(request,"username already exists")
                return redirect("register")
            else:
                user=User.objects.create_user(username=name,password=passw)
            user.save()
            return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('submit_form')
        else:
            messages.info(request,"invalid username or password")
            return redirect('login')

    return render(request,'login.html')






def logout(request):
    return redirect('demo')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        courses = request.POST.get('courses')

        student=Student(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            department=department,
            courses=courses
        )
        existing_student = Student.objects.filter(name=name,dob=dob,age=age,gender=gender, email=email, phone=phone,address=address,department=department,courses=courses).first()
        if existing_student:
            messages.info(request, "Student already submitted the form once.So couldnt submit the form")
            return redirect('submit_form')
        student.save()
        if Student.objects.exists():
            messages.info(request, "form submitted successfully")
    return render(request, 'form.html',)



