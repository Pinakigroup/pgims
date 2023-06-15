from django.shortcuts import render, redirect
from .forms import WorkOrderForm
from django.contrib import messages

# Create your views here.

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