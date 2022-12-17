from django.shortcuts import render, get_object_or_404, redirect
from .models import FabricRequisition
from .forms import FabricRequisitionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.

# Create
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def create(request):
    form = FabricRequisitionForm()
    if request.method == 'POST':
        form = FabricRequisitionForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Fabric Requisition created successfully')
            return redirect('fabricRequis_read')
    context= {
        'form': form
    }
    return render(request, 'fabric_requisition/create.html', context)


# Read
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def fabricRequis_read(request):
    
    fabricRequis_data = FabricRequisition.objects.all().order_by('-id')
    context = {
        'fabricRequis_data': fabricRequis_data
    }
    return render(request, 'fabric_requisition/read.html', context)

# Update
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def fabricRequis_update(request, pk):
    get_fabricRequis_data = get_object_or_404(FabricRequisition, pk=pk)
    form = FabricRequisitionForm(instance=get_fabricRequis_data)
    if request.method == 'POST':
        form = FabricRequisitionForm(request.POST, instance=get_fabricRequis_data)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Fabric Requisition updated successfully')
            return redirect('fabricRequis_read')
    context = {
        'form': form
    }    
    return render(request, 'fabric_requisition/update.html', context)

# Delete
@login_required
@allowed_users(allowed_roles=['admin', 'store'])
def fabricRequis_delete(request, pk):
    get_fabricRequis = get_object_or_404(FabricRequisition, pk=pk)
    get_fabricRequis.delete()
    # messages.error(request, 'Fabric Requisition deleted successfully')
    return redirect('fabricRequis_read')