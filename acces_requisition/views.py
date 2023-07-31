from django.shortcuts import render, redirect, get_object_or_404
from stock.models import Stock
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import AccesRequisitionBill, AccesRequisitionBillDetails, AccesRequisitionItem
from .forms import AccesRDetailsForm, AccesRItemFormset, AccesRForm, AccesRItemForm, AccesRequisitionBillDateSearchForm
from django.views.generic import (
    View, 
    ListView,
    DeleteView,
)
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.utils.decorators import method_decorator
from .forms import UserUpdateForm
# Create your views here.

# Create
@method_decorator(login_required, name='dispatch')
class AccesRCreateView(View):                                                      
    template_name = 'acces_requisition/create.html'

    def get(self, request):
        form = AccesRForm(request.GET or None)
        formset = AccesRItemFormset(request.GET or None)                          # renders an empty formset
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
        form = AccesRForm(request.POST)
        formset = AccesRItemFormset(request.POST)                                 # recieves a post method for the formset
        if form.is_valid() and formset.is_valid():
            # saves bill
            billobj = form.save(commit=False)
            billobj.save()     
            # create bill details object
            # billdetailsobj = AccesRequisitionBillDetails(billno=billobj)
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
            return redirect('ar_read')
        form = AccesRForm(request.GET or None)
        formset = AccesRItemFormset(request.GET or None)
        context = {
            'form'      : form,
            'formset'   : formset,
        }
        return render(request, self.template_name, context)
    
    
# Read
# @login_required
# @allowed_users(allowed_roles=['admin', 'store'])
# class AccesRView(ListView):
#     model = AccesRequisitionBill 
#     template_name = 'acces_requisition/read.html'
#     context_object_name = 'bills'
#     ordering = ['-time']

@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def accesR_read(request):
    form = AccesRequisitionBillDateSearchForm(request.POST or None)
    bills = AccesRequisitionBill.objects.all().order_by('-time')
    context = {
        'bills':bills,
        'form':form,
    }
    if request.method == 'POST':
        bills = AccesRequisitionBill.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'bills':bills,
        'form':form,
    }
    return render(request, 'acces_requisition/read.html', context)

# @login_required
# @allowed_users(allowed_roles=['admin', 'store'])
@method_decorator(login_required, name='dispatch')
class AccesRBillView(View):
    model = AccesRequisitionBill
    template_name = "bill/ar_bill.html"
    
    def get(self, request, billno):
        context = {
            'bill'          : AccesRequisitionBill.objects.get(billno=billno),
            'items'         : AccesRequisitionItem.objects.filter(billno=billno),
        }
        return render(request, self.template_name, context)

    def post(self, request, billno):
        form = AccesRDetailsForm(request.POST)
        if form.is_valid():
            billdetailsobj = AccesRequisitionBillDetails.objects.get(billno=billno)
            
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
            'bill'          : AccesRequisitionBill.objects.get(billno=billno),
            'items'         : AccesRequisitionItem.objects.filter(billno=billno),
            'billdetails'   : AccesRequisitionBillDetails.objects.get(billno=billno),
        }
        return render(request, self.template_name, context)
    
#  Delete     
# @login_required
# @allowed_users(allowed_roles=['admin'])   
# AttributeError: 'function' object has no attribute 'as_view'  -->> solution:  Since, this view is a clasbase view . goto--->> urls.py/ and .as_view() (remove)
@method_decorator(login_required, name='dispatch')
class AccesRDeleteView(SuccessMessageMixin, DeleteView):
    model = AccesRequisitionBill
    template_name = "acces_requisition/delete.html"
    success_url = '/acces_requisition'
    
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = AccesRequisitionItem.objects.filter(billno=self.object.billno)
        for item in items:
            stock = get_object_or_404(Stock, name=item.stock.name)
            if stock.is_deleted == False:
                stock.quantity += item.quantity
                stock.save()
        messages.success(self.request, "Accessories items has been deleted successfully")
        return super(AccesRDeleteView, self).delete(*args, **kwargs)