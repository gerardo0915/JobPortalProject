from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserType 
from .forms import RegistrationForm, CustomAuthenticationForm

def login_view(request):
    # Handle user login
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            user_type = UserType.objects.get(user=user).user_type
            if user_type == 'employer':
                return redirect('employer_jobs')
            else:
                return redirect('job_list')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    # Handle user logout
    logout(request)
    return redirect('job_list')  

def register_view(request):
    # Handle user registration
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data.get('user_type') 
            UserType.objects.create(user=user, user_type=user_type)          
            return redirect('user_accounts:login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})