from django.shortcuts import render, get_object_or_404, redirect
from .models import StoreReceiver
from .forms import StoreReceiverForm, StoreReceiverDateSearchForm
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.

# Create
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def create(request):
    if request.method == 'POST':
        form = StoreReceiverForm(request.POST)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid() and u_form.is_valid():
            u_form.save()
            form.save()
            messages.success(request, 'Store Receiver created successfully')
            return redirect('storeRec_read')
    else:
        form = StoreReceiverForm()
        u_form = UserUpdateForm(instance=request.user)
    context= {
        'form': form,
        'u_form': u_form,
    }
    return render(request, 'store_receiver/create.html', context)


# Read
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def storeRec_read(request):
    form = StoreReceiverDateSearchForm(request.POST or None)
    storeRec_data = StoreReceiver.objects.all().order_by('-id')
    context = {
        'storeRec_data': storeRec_data,
        'form':form,
    }
    if request.method == 'POST':
        storeRec_data = StoreReceiver.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'storeRec_data': storeRec_data,
        'form':form,
    }
    return render(request, 'store_receiver/read.html', context)

# Update
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def storeRec_update(request, pk):
    get_storeRec_data = get_object_or_404(StoreReceiver, pk=pk)
    form = StoreReceiverForm(instance=get_storeRec_data)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        form = StoreReceiverForm(request.POST, instance=get_storeRec_data)
        if form.is_valid() and u_form.is_valid():
            u_form.save()
            form.save()
            messages.success(request, 'Store Receiver updated successfully')
            return redirect('storeRec_read')
        
    else:
        form = StoreReceiverForm(instance=get_storeRec_data)
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'form': form,
        'u_form': u_form,
    }    
    return render(request, 'store_receiver/update.html', context)

# Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def storeRec_delete(request, pk):
    get_storeRec = get_object_or_404(StoreReceiver, pk=pk)
    get_storeRec.delete()
    messages.error(request, 'Store Receiver deleted successfully')
    return redirect('storeRec_read')
