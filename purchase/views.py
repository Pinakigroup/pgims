from django.shortcuts import render, get_object_or_404, redirect
from .forms import PurchaseForm
from .models import Purchase
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.

# Create 
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser'])
def create(request):
    form = PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Purchase created successfully')
            return redirect('create')
    context = {
        'form': form
    }
    return render(request, 'purchase/create.html', context)

# Read 
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser'])
def purchase_read(request):
    purchase_data = Purchase.objects.all().order_by('-id')
    context = {
        'purchase_data': purchase_data
    }  
    return render(request, 'purchase/read.html', context)

# Update 
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser'])
def purchase_update(request, pk):
    get_purchase_data = get_object_or_404(Purchase, pk=pk)
    form = PurchaseForm(instance=get_purchase_data)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=get_purchase_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Purchase updated successfully')
            return redirect('purchase_read')
    context = {
        'form': form
    }
    return render(request, 'purchase/update.html', context)

# Delete 
@login_required
@allowed_users(allowed_roles=['admin'])
def purchase_delete(request, pk):
    get_purchase = get_object_or_404(Purchase, pk=pk)
    get_purchase.delete()
    messages.error(request, 'Purchase delete successfully')
    return redirect('purchase_read')
