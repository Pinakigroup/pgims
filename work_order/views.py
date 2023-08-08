from django.shortcuts import render, redirect
from .forms import WorkOrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.


# Create
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def create(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Work Order created')
            # Process the forms and redirect
            return redirect('create') 
    else:
        form = WorkOrderForm()
        
    context= {
        'form': form
    }
    return render(request, 'work_order/create.html', context)