from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import JobForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials!!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect("register")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            print('user created successfully')
            return redirect("login")
        
        
    else:
        return render(request, 'register.html')

def main(request):
    return render(request, 'main.html')

def logout(request):
    auth.logout(request)
    return redirect("login")

def Job(request):
    messages.info(request, 'Your form is submitted')
    return redirect('main')
        
        