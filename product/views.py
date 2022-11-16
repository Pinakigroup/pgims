from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# Create 
@login_required
def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully')
            return redirect('product_read')
    context = {
        'form': form
    }
    return render(request, 'product/create.html', context)

# Read 
@login_required
def product_read(request):
    product_data = Product.objects.all().order_by('-id')
    context = {
        'product_data': product_data
    }
    return render(request, 'product/read.html', context)

# Update 
@login_required
def product_update(request, pk):
    get_product_data = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=get_product_data)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=get_product_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('product_read')
    context = {
        'form': form
    }
    return render(request, 'product/update.html', context)

# Delete
@login_required
def product_delete(request, pk):
    get_product = get_object_or_404(Product, pk=pk)
    get_product.delete()
    messages.error(request, 'Product delete successfully')
    return redirect('product_read')