from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from users.forms import CustomUserRegisterForm



# Create your views here.


def user_register(request):
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:blog-list')
    else:
        form = CustomUserRegisterForm()
    return render(request, 'users/user-register.html', {"myform": form })


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('blog:blog-list')
        else:
            messages.error(request, "🚨Invalid Username or Password🚨")
    
    else:
        form = AuthenticationForm()
    return render(request, 'users/user-login.html', {"inform": form})


def user_logout(request):
    
    if request.method == "POST":
        logout(request)
        return redirect('users:user-login')
    return render(request, 'users/user-logout.html')