from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "superadmin/index.html")

def admin_registration(request):
    return render(request, "superadmin/registration.html")

def admin_login(request):
    return render(request, 'superadmin/login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  
            user.is_superuser = True  
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login') 
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):    
    if request.method == 'POST':
        email = request.POST['email']
        raw_password = request.POST['raw_password']
        user = authenticate(request, email=email, password=raw_password)
        if user is not None and user.is_superuser: 
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'registration/login.html')

def admin_dashboard(request):
    return render(request, 'superadmin/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')


