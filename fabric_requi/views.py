from django.shortcuts import render, redirect, get_object_or_404
from stock.models import Stock
from store.models import StoreBill
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users
from django.contrib.messages.views import SuccessMessageMixin
from .models import FabricRequisitionBill, FabricRequisitionBillDetails, FabricRequisitionItem
from .forms import FabricRDetailsForm, FabricRItemFormset, FabricRForm, FabricRItemForm, FabricRequisitionBillDateSearchForm
from django.views.generic import (View, ListView, DeleteView,)
from .forms import UserUpdateForm

# Create your views here

# Create
@method_decorator(login_required, name='dispatch')
class FabricRequiCreateView(View):                                                      
    template_name = 'fabric_requi/create.html'

    def get(self, request):

        form = FabricRForm(request.GET or None)
        formset = FabricRItemFormset(request.GET or None)                          # renders an empty formset
        stocks = Stock.objects.filter(is_deleted=False)
        # Show user name in hare
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
        else:
            u_form = UserUpdateForm(instance=request.user)
            
        context = {
            'form'      : form,
            'formset'   : formset,
            'stocks'    : stocks, 
            'u_form'    : u_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):        
        form = FabricRForm(request.POST)
        formset = FabricRItemFormset(request.POST)                                 # recieves a post method for the formset
        if form.is_valid() and formset.is_valid():
            # saves bill
            billobj = form.save(commit=False)
            billobj.save()     
            # create bill details object
            # billdetailsobj = FabricRequisitionBillDetails(billno=billobj)
            # billdetailsobj.save()
            for form in formset:                                                # for loop to save each individual form as its own object
                # false saves the item and links bill to the item
                billitem = form.save(commit=False)
                billitem.billno = billobj                                       # links the bill object to the items
                # gets the stock item
                stock = get_object_or_404(Stock, name=billitem.stock.name)  
                # calculates the total price
                # billitem.totalprice = billitem.unit_price * billitem.quantity
                # updates quantity in stock db
                stock.quantity -= billitem.quantity             

                # saves bill item and stock
                stock.save()
                billitem.save()
            messages.success(request, "Sold items have been registered successfully")
            return redirect('fabricr_read')
        form = FabricRForm(request.GET or None)
        formset = FabricRItemForm(request.GET or None)   
                           
        context = {
            'form'      : form,
            'formset'   : formset,
        }
        return render(request, self.template_name, context)
    
# class base List View 

# class FabricRequiView(ListView):
#     model = FabricRequisitionBill 
#     template_name = 'fabric_requi/read.html'
#     context_object_name = 'bills'
#     ordering = ['-time']

# Read
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def fabricRequi_read(request):
    form = FabricRequisitionBillDateSearchForm(request.POST or None)
    bills = FabricRequisitionBill.objects.all().order_by('-time')
    context = {
        'bills':bills,
        'form':form,
    }
    if request.method == 'POST':
        bills = FabricRequisitionBill.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'bills':bills,
        'form':form,
    }
    return render(request, 'fabric_requi/read.html', context)

# Fabric Report Read
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def fabricReport_read(request):
    form = FabricRequisitionBillDateSearchForm(request.POST or None)
    bills = FabricRequisitionBill.objects.all().order_by('-time')
    context = {
        'bills':bills,
        'form':form,
    }
    if request.method == 'POST':
        bills = FabricRequisitionBill.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'bills':bills,
        'form':form,
    }
    return render(request, 'fabric_requi/report.html', context)

    
@method_decorator(login_required, name='dispatch')
class FabricRequiBillView(View):
    model = FabricRequisitionBill
    template_name = "bill/fr_bill.html"
    
    def get(self, request, billno):
        context = {
            'bill'          : FabricRequisitionBill.objects.get(billno=billno),
            'items'         : FabricRequisitionItem.objects.filter(billno=billno),
        }
        return render(request, self.template_name, context)

    def post(self, request, billno):
        form = FabricRDetailsForm(request.POST)
        if form.is_valid():
            billdetailsobj = FabricRequisitionBillDetails.objects.get(billno=billno)
            
            billdetailsobj.eway = request.POST.get("eway")    
            billdetailsobj.veh = request.POST.get("veh")
            billdetailsobj.destination = request.POST.get("destination")
            billdetailsobj.po = request.POST.get("po")
            billdetailsobj.cgst = request.POST.get("cgst")
            billdetailsobj.sgst = request.POST.get("sgst")
            billdetailsobj.igst = request.POST.get("igst")
            billdetailsobj.cess = request.POST.get("cess")
            billdetailsobj.tcs = request.POST.get("tcs")
            billdetailsobj.total = request.POST.get("total")

            billdetailsobj.save()
            messages.success(request, "Bill details have been modified successfully")
        context = {
            'bill'          : FabricRequisitionBill.objects.get(billno=billno),
            'items'         : FabricRequisitionItem.objects.filter(billno=billno),
            'billdetails'   : FabricRequisitionBillDetails.objects.get(billno=billno),
        }
        return render(request, self.template_name, context)
    
    

@method_decorator(login_required, name='dispatch')
class FabricRequiDeleteView(SuccessMessageMixin, DeleteView):
    model = FabricRequisitionBill
    template_name = "fabric_requi/delete.html"
    success_url = '/fabric_requi'
    
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = FabricRequisitionItem.objects.filter(billno=self.object.billno)
        for item in items:
            stock = get_object_or_404(Stock, name=item.stock.name)
            if stock.is_deleted == False:
                stock.quantity += item.quantity
                stock.save()
        messages.success(self.request, "Fabric items has been deleted successfully")
        return super(FabricRequiDeleteView, self).delete(*args, **kwargs)