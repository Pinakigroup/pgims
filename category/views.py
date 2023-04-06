from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm, CategoryDateSearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.

# Create
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def create(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully')
            return redirect('category_read')
    context= {
        'form': form
    }
    return render(request, 'category/create.html', context)


# Read
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def category_read(request):
    form = CategoryDateSearchForm(request.POST or None)
    category_data = Category.objects.all().order_by('-id')
    context = {
        'category_data': category_data,
        'form':form,
    }
    if request.method == 'POST':
        category_data = Category.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'category_data': category_data,
        'form':form,
    }
    return render(request, 'category/read.html', context)

# Update
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def category_update(request, pk):
    get_category_data = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=get_category_data)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=get_category_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully')
            return redirect('category_read')
    context = {
        'form': form
    }    
    return render(request, 'category/update.html', context)

# Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def category_delete(request, pk):
    get_category = get_object_or_404(Category, pk=pk)
    get_category.delete()
    messages.error(request, 'Category deleted successfully')
    return redirect('category_read')