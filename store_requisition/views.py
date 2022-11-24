from django.shortcuts import render, get_object_or_404, redirect
from .models import StoreRequisition
from .forms import StoreRequisitionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# Create
@login_required
def create(request):
    form = StoreRequisitionForm()
    if request.method == 'POST':
        form = StoreRequisitionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Store Requisition created successfully')
            return redirect('storeRequis_read')
    context= {
        'form': form
    }
    return render(request, 'store_requisition/create.html', context)


# Read
@login_required
def storeRequis_read(request):
    
    storeRequis_data = StoreRequisition.objects.all().order_by('-id')
    context = {
        'storeRequis_data': storeRequis_data
    }
    return render(request, 'store_requisition/read.html', context)

# Update
@login_required
def storeRequis_update(request, pk):
    get_storeRequis_data = get_object_or_404(StoreRequisition, pk=pk)
    form = StoreRequisitionForm(instance=get_storeRequis_data)
    if request.method == 'POST':
        form = StoreRequisitionForm(request.POST, instance=get_storeRequis_data)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Store Requisition updated successfully')
            return redirect('storeRequis_read')
    context = {
        'form': form
    }    
    return render(request, 'store_requisition/update.html', context)

# Delete
@login_required
def storeRequis_delete(request, pk):
    get_storeRequis = get_object_or_404(StoreRequisition, pk=pk)
    get_storeRequis.delete()
    # messages.error(request, 'Store Requisition deleted successfully')
    return redirect('storeRequis_read')
