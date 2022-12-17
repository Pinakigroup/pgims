from django.shortcuts import render, get_object_or_404, redirect
from .models import StoreReceiver
from .forms import StoreReceiverForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.

# Create
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def create(request):
    form = StoreReceiverForm()
    if request.method == 'POST':
        form = StoreReceiverForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Store Receiver created successfully')
            return redirect('storeRec_read')
    context= {
        'form': form
    }
    return render(request, 'store_receiver/create.html', context)


# Read
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def storeRec_read(request):
    storeRec_data = StoreReceiver.objects.all().order_by('-id')
    context = {
        'storeRec_data': storeRec_data
    }
    return render(request, 'store_receiver/read.html', context)

# Update
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def storeRec_update(request, pk):
    get_storeRec_data = get_object_or_404(StoreReceiver, pk=pk)
    form = StoreReceiverForm(instance=get_storeRec_data)
    if request.method == 'POST':
        form = StoreReceiverForm(request.POST, instance=get_storeRec_data)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Store Receiver updated successfully')
            return redirect('storeRec_read')
    context = {
        'form': form
    }    
    return render(request, 'store_receiver/update.html', context)

# Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def storeRec_delete(request, pk):
    get_storeRec = get_object_or_404(StoreReceiver, pk=pk)
    get_storeRec.delete()
    # messages.error(request, 'Store Receiver deleted successfully')
    return redirect('storeRec_read')
