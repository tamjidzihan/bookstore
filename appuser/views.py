from django.shortcuts import render,redirect
from django.contrib import messages
from core.models import User
from django.contrib import auth
from .forms import CreateUserFrom

# Create your views here.

def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username is Alrady Exist')
                return redirect('/appuser/register/')
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email is Alrady Exist')
                return redirect('/appuser/register/')
            else:
                user = User.objects.create_user(
                    username = username,
                    password = password,
                    email = email
                    )
                user.set_password(password)
                print("success")
                user.save()
                return redirect('/appuser/log-in/')
        else:
            messages.info(request,'Password Do not Match')
            return redirect('/appuser/register/')
    return render(request,'appuser/register.html')
            

def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            return redirect('/')
        else:
            messages.info(request,"Invalid Username And Password")
            return redirect('/appuser/log-in/')
    return render(request,'appuser/login.html')


def registration_error(request):
    return  render(request,'appuser/registration_error.html')