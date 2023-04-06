from django.shortcuts import render, get_object_or_404, redirect
from .models import Merchandiser
from .forms import MerchandiserForm, MerchandiserDateSearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.

# Create 
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser'])
def create(request):
    form = MerchandiserForm()
    if request.method == 'POST':
        form = MerchandiserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Merchandiser created successfully')
            return redirect('merchandiser_read')
    context = {
        'form': form
    }
    return render(request, 'merchandiser/create.html', context)

# Read 
@allowed_users(allowed_roles=['admin', 'merchandiser'])
@login_required
def merchandiser_read(request):
    form = MerchandiserDateSearchForm(request.POST or None)
    merchandiser_data = Merchandiser.objects.all().order_by('-id')
    context = {
        'merchandiser_data': merchandiser_data,
        'form':form,
    }  
    if request.method == 'POST':
        merchandiser_data = Merchandiser.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'merchandiser_data': merchandiser_data,
        'form':form,
    }
    return render(request, 'merchandiser/read.html', context)

# Update 
@allowed_users(allowed_roles=['admin', 'merchandiser'])
@login_required
def merchandiser_update(request, pk):
    get_merchandiser_data = get_object_or_404(Merchandiser, pk=pk)
    form = MerchandiserForm(instance=get_merchandiser_data)
    if request.method == 'POST':
        form = MerchandiserForm(request.POST, request.FILES, instance=get_merchandiser_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Merchandiser updated successfully')
            return redirect('merchandiser_read')
    context = {
        'form': form
    }
    return render(request, 'merchandiser/update.html', context)

# Delete 
@allowed_users(allowed_roles=['admin'])
@login_required
def merchandiser_delete(request, pk):
    get_merchandiser = get_object_or_404(Merchandiser, pk=pk)
    get_merchandiser.delete()
    messages.error(request, 'Merchandiser deleted successfully')
    return redirect('merchandiser_read')
    