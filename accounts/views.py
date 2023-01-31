from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from pgims.forms import RegisterForm, UserUpdateForm
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

# Login
@unauthenticated_user
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
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name="new")
            user.groups.add(group)
             
            messages.success(request, 'Account was created for ' + username)
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


# Create 
# @login_required

def profile(request):
    # player, created = Profile.objects.get_or_create(user=request.user)
    # Profile.objects.get_or_create(user=request.user_acc)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            user_name = p_form.cleaned_data.get('user')
            messages.success(request, f'{user_name} has been added')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)