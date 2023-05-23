from django.shortcuts import render, get_object_or_404, redirect
from .models import Buyer
from .forms import BuyerForm, BuyerDateSearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
# Create your views here.


# Create
def create(request):
    form = BuyerForm()
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Buyer created successfully')
            return redirect('buyer_read')
    context= {
        'form': form
    }
    return render(request, 'buyer/create.html', context)

# Read
def buyer_read(request):
    form = BuyerDateSearchForm(request.POST or None)
    buyer_data = Buyer.objects.all().order_by('-id')
    context = {
        'buyer_data': buyer_data,
        'form':form,
    }
    if request.method == 'POST':
        buyer_data = Buyer.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'buyer_data': buyer_data,
        'form':form,
    }
    return render(request, 'buyer/read.html', context)

def buyer_update(request, pk):
    get_buyer_data = get_object_or_404(Buyer, pk=pk)
    form = BuyerForm(instance=get_buyer_data)
    if request.method == 'POST':
        form = BuyerForm(request.POST, instance=get_buyer_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Buyer updated successfully')
            return redirect('buyer_read')
    context = {
        'form': form
    }
    return render(request, 'buyer/update.html', context)

def buyer_delete(request, pk):
    get_buyer = get_object_or_404(Buyer, pk=pk)
    get_buyer.delete()
    messages.error(request, 'buyer deleted successfully')
    return redirect('buyer_read')