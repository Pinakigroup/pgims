from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View, CreateView, UpdateView, ListView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Stock
from .forms import StockForm, StockDateSearchForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.utils.decorators import method_decorator

# Create your views here.

# Create 
@method_decorator(login_required, name='dispatch')
class StockCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "stock/create.html"                                                 # 'edit_stock.html' used as the template
    success_url = '/stock'                                                                 # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been created successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        return context  

# Read
# class StockListView(ListView):
#     model = Stock 
#     template_name = 'stock/read.html'
#     context_object_name = 'stocks'
#     paginate_by = 10
    
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def stock_read(request):
    form = StockDateSearchForm(request.POST or None)
    stocks = Stock.objects.all().order_by('-id')
    context = {
        'stocks': stocks,
        'form':form,
    }
    if request.method == 'POST':
        stocks = Stock.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'stocks': stocks,
        'form':form,
    }
    return render(request, 'stock/read.html', context)

# Update 
@method_decorator(login_required, name='dispatch')
class StockUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "stock/update.html"                                                 # 'edit_stock.html' used as the template
    success_url = '/stock'                                                              # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been updated successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        return context

# Delete 
@login_required
@allowed_users(allowed_roles=['admin'])
def stock_delete(request, pk):
    get_stock = get_object_or_404(Stock, pk=pk)
    get_stock.delete()
    messages.error(request, 'Stock delete successfully')
    return redirect('stock_read')

