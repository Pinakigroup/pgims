from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from category.models import Category
from pgims.forms import RegisterForm
from product.models import Product
from supplier.models import Supplier
from merchandiser.models import Merchandiser
from purchase.models import Purchase
from store.models import Store
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    total_category = Category.objects.count()
    total_product = Product.objects.count()
    total_merchandiser = Merchandiser.objects.count()
    total_supplier = Supplier.objects.count()
    total_purchase = Purchase.objects.count()
    total_store = Store.objects.count()
    stores = Store.objects.all().order_by('-id')
    
    context = {
        'name': total_category,
        'description': total_product,
        'office_id': total_merchandiser,
        'supplier_name': total_supplier,
        'style_detail': total_purchase,
        'style': total_store,
        'stores': stores
    }
    return render(request, 'home.html', context)

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
def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successfully, you can login now...')
            return redirect('login')
    context = {
        'form': form
    }    
    return render(request, 'register.html', context)

#  logout
def logout_view(request):
    logout(request)
    return redirect('login')

# User Profile
@login_required
def profile(request):
    user_data = User.objects.all()
    context = {
        'user_data': user_data
    } 
    return render(request, 'users/profile.html', context)

