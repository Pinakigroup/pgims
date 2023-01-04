from django.shortcuts import render, redirect, get_object_or_404
from stock.models import Stock
from django.contrib import messages
from .models import PurchaseBill, PurchaseBillDetails, PurchaseItem
from .forms import PurchaseDetailsForm, PurchaseItemFormset, PurchaseForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    View, 
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.

# used to generate a bill object and save items
class PurchaseCreateView(View):                                                 
    template_name = 'purchase_order/create.html'
    
    def get(self, request):
        form = PurchaseForm(request.GET or None)
        formset = PurchaseItemFormset(request.GET or None)                       # renders an empty formset
        stocks = Stock.objects.filter(is_deleted=False)
        context = {
            'form'      : form,
            'formset'   : formset,
            'stocks'    : stocks  
        }                                                                        # sends the supplier and formset as context
        return render(request, self.template_name, context)

    def post(self, request):
        form = PurchaseForm(request.POST)
        formset = PurchaseItemFormset(request.POST) 
        # recieves a post method for the formset
        
        if form.is_valid() and formset.is_valid():
            # saves bill
            billobj = form.save(commit=False)
            billobj.save() 
            
            for form in formset:                                                   # for loop to save each individual form as its own object
                # false saves the item and links bill to the item
                billitem = form.save(commit=False)
                billitem.billno = billobj               

                # gets the stock item
                stock = get_object_or_404(Stock, name=billitem.stock.name)         # gets the item
                # calculates the total price
                billitem.totalprice = billitem.unit_price * billitem.quantity
                
                # updates quantity in stock db
                # stock.quantity += billitem.quantity                               # updates quantity
                
                # saves bill item and stock
                stock.save()
                billitem.save()
            messages.success(request, "Purchased items have been registered successfully")
            return redirect('po_read')
        form = PurchaseForm(request.GET or None)
        formset = PurchaseItemFormset(request.GET or None)
        context = {
            'form'      : form,
            'formset'   : formset,            
        }
        return render(request, self.template_name, context)    
    
# Read
class PurchaseView(ListView):
    model = PurchaseBill 
    template_name = 'purchase_order/read.html'
    context_object_name = 'bills'
    ordering = ['-time']


# used to display the purchase bill object
class PurchaseBillView(View):
    model = PurchaseBill
    template_name = "bill/po_bill.html"
    # bill_base = "bill/purchase_bill.html"

    def get(self, request, billno):
        context = {
            'bill'          : PurchaseBill.objects.get(billno=billno),
            'items'         : PurchaseItem.objects.filter(billno=billno),
            # 'billdetails'   : PurchaseBillDetails.objects.get(billno=billno),
            # 'bill_base'     : self.bill_base,
        }
        return render(request, self.template_name, context)

    def post(self, request, billno):
        form = PurchaseDetailsForm(request.POST)
        if form.is_valid():
            billdetailsobj = PurchaseBillDetails.objects.get(billno=billno)
            
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
            'bill'          : PurchaseBill.objects.get(billno=billno),
            'items'         : PurchaseItem.objects.filter(billno=billno),
            'billdetails'   : PurchaseBillDetails.objects.get(billno=billno),
            # 'bill_base'     : self.bill_base,
        }
        return render(request, self.template_name, context)
    
# class PurchaseDeleteView(SuccessMessageMixin, DeleteView):
#     model = PurchasesBill
#     # template_name = "purchases/delete_purchase.html"
#     success_url = '/purchases'
    
#     def delete(self, *args, **kwargs):
#         self.object = self.get_object()
#         items = PurchasesItem.objects.filter(billno=self.object.billno)
#         for item in items:
#             stock = get_object_or_404(Stock, name=item.stock.name)
#             if stock.is_deleted == False:
#                 stock.quantity -= item.quantity
#                 stock.save()
#         messages.success(self.request, "Purchase bill has been deleted successfully")
#         return super(PurchaseDeleteView, self).delete(*args, **kwargs)
