from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from pgims.forms import RegisterForm
from django.contrib.auth.models import User
from .decorators import unauthenticated_user

# Create your views here.

# Login
def login_view(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user_auth = authenticate(username = u, password = p)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, 'Login Successfully')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username and password')
    return render(request, 'login.html')    

# Registration
@unauthenticated_user
def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    context = {
        'form': form
    }    
    return render(request, 'register.html', context)



#  logout
def logout_view(request):
    logout(request)
    return redirect('login')

# User Profile
def profile(request):
    user_data = User.objects.all()
    context = {
        'user_data': user_data
    } 
    return render(request, 'users/profile.html', context)