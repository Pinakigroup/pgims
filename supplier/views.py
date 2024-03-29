from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier
from .forms import SupplierForm, SupplierDateSearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.

# Create 
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser'])
def create(request):
    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier created successfully')
            return redirect('supplier_read')
    context = {
        'form': form
    }
    return render(request, 'supplier/create.html', context)

# Read 
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser'])
def supplier_read(request):
    form = SupplierDateSearchForm(request.POST or None)
    supplier_data = Supplier.objects.all().order_by('-id')
    context = {
        'supplier_data': supplier_data,
        'form':form,
    }
    if request.method == 'POST':
        supplier_data = Supplier.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'supplier_data': supplier_data,
        'form':form,
    }
    return render(request, 'supplier/read.html', context)


# Update 
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser'])
def supplier_update(request, pk):
    get_supplier_data = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(instance=get_supplier_data)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=get_supplier_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier updated successfully')
            return redirect('supplier_read')
    context = {
        'form': form
    }
    return render(request, 'supplier/update.html', context)

# Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def supplier_delete(request, pk):
    get_supplier = get_object_or_404(Supplier, pk=pk)
    get_supplier.delete()
    messages.error(request, 'Supplier delete successfully')
    return redirect('supplier_read')