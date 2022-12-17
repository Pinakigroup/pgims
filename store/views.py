from django.shortcuts import render, get_object_or_404, redirect
from .forms import StoreForm
from .models import Store
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.

# Create 
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def create(request):
    form = StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Store create successfully')
            return redirect('store_read')
        else:
            messages.error(request, 'Store form is not valide')
    context = {
        'form': form
    }    
    return render(request, 'store/create.html', context)

# Read 
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def store_read(request):
    store_data = Store.objects.all().order_by('-id')
    context = {
        'store_data': store_data
    }  
    return render(request, 'store/read.html', context)


# Update 
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def store_update(request, pk):
    get_store_data = get_object_or_404(Store, pk=pk)
    form = StoreForm(instance=get_store_data)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=get_store_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Store updated successfully')
            return redirect('store_read')
    context = {
        'form': form
    }
    return render(request, 'store/update.html', context)

# Delete 
@login_required
@allowed_users(allowed_roles=['admin'])
def store_delete(request, pk):
    get_store = get_object_or_404(Store, pk=pk)
    get_store.delete()
    messages.error(request, 'Store delete successfully')
    return redirect('store_read')
