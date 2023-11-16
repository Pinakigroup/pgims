from django.shortcuts import render, redirect, get_object_or_404
from stock.models import Stock
from django.contrib import messages
from .models import StoreBill, StoreItem, StoreBillDetails
from .forms import StoreDetailsForm, StoreItemFormset, StoreForm, StoreItemForm, StockSearchForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    View, 
    ListView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import StoreBillSerializer, StoreItemSerializer, StoreAccessoriesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import UserUpdateForm
from django.db import transaction

# Create your views here.

# used to generate a bill object and save items
@method_decorator(login_required, name='dispatch')
class StoreCreateView(LoginRequiredMixin, View):                                                 
    template_name = 'store/create.html'
    
    def get(self, request):
        form = StoreForm(request.GET or None)
        formset = StoreItemFormset(request.GET or None)                       # renders an empty formset
        stocks = Stock.objects.filter(is_deleted=False)
        
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
        }                                                                        # sends the supplier and formset as context
        return render(request, self.template_name, context)

    @transaction.atomic()
    def post(self, request):
        work_order = request.POST["work_order"]
        bill_obj = StoreBill.objects.filter(work_order=work_order).first()
        if bill_obj:
            form = StoreForm(request.POST, request.FILES, instance=bill_obj)
        else:
            form = StoreForm(request.POST, request.FILES)
        formset = StoreItemFormset(request.POST) 
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
                # updates quantity in stock db
                stock.quantity += billitem.quantity                               # updates quantity
                
                billitem.stock_qty = stock.quantity - billitem.quantity                            # updates quantity
                # saves bill item and stock
                stock.save()
                
                billitem.save()
            messages.success(request, "Store items have been registered successfully")
            return redirect('store_read')
        else:
            form = StoreForm(request.GET or None)
            formset = StoreItemFormset(request.GET or None)
        context = {
            'form': form,
            # 'formset': formset,
        }
        return render(request, self.template_name, context)    

# Read
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def store_read(request):
    form = StockSearchForm(request.POST or None)
    bills = StoreBill.objects.all().order_by('-time')
    context = {
        'bills':bills,
        'form':form,
    }
    if request.method == 'POST':
        bills = StoreBill.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'bills':bills,
        'form':form,
    }
    return render(request, 'store/read.html', context)

# Store Report Read
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def storeReport_read(request):
    form = StockSearchForm(request.POST or None)
    bills = StoreBill.objects.all().order_by('-time')
    context = {
        'bills':bills,
        'form':form,
    }
    if request.method == 'POST':
        bills = StoreBill.objects.filter(
										updated_at__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'bills':bills,
        'form':form,
    }
    return render(request, 'store/report.html', context)


# used to display the purchase bill object
@method_decorator(login_required, name='dispatch')
class StoreBillView(View):
    model = StoreBill
    template_name = "bill/store_bill.html"
    # bill_base = "bill/purchase_bill.html"

    def get(self, request, billno):
        context = {
            'bill'          : StoreBill.objects.get(billno=billno),
            'items'         : StoreItem.objects.filter(billno=billno),
            # 'billdetails'   : StoreBillDetails.objects.get(billno=billno),
            # 'bill_base'     : self.bill_base,
        }
        return render(request, self.template_name, context)

    def post(self, request, billno):
        form = StoreDetailsForm(request.POST)
        if form.is_valid():
            billdetailsobj = StoreBillDetails.objects.get(billno=billno)
            
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
            'bill'          : StoreBill.objects.get(billno=billno),
            'items'         : StoreItem.objects.filter(billno=billno),
            'billdetails'   : StoreBillDetails.objects.get(billno=billno),
            # 'bill_base'     : self.bill_base,
        }
        return render(request, self.template_name, context)

    
# Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def store_delete(request, pk):
    get_store = get_object_or_404(StoreBill, pk=pk)
    # Retrieve items associated with the store bill
    items = StoreItem.objects.filter(billno=get_store.billno)
    for item in items:
        stock = get_object_or_404(Stock, name=item.stock.name)
        if not stock.is_deleted:
            stock.quantity -= item.quantity
            stock.save()
    get_store.delete()
    messages.error(request, 'Store item has been deleted successfully')
    return redirect('store_read')
    
    
class StoreBillDetailView(APIView):
    # def get(self, request, pk):
    #     try:
    #         store = StoreBill.objects.get(pk=pk)
    #         serializer = StoreBillSerializer(store)
    #         return Response(serializer.data)
    #     except StoreBill.DoesNotExist:
    #         return Response(status=404)

    def get(self, request, pk):
        try:
            store = StoreBill.objects.get(pk=pk)
            serializer = StoreBillSerializer(store)

            # Get related Store Items and serialize them
            store_items = store.storebillno.all()  # Assuming your related name is 'storeitem_set'
            store_items_serializer = StoreItemSerializer(store_items, many=True)  # You need to create storeItemSerializer
            
            print("LPLPLPLPLPLPLPLP", store_items_serializer.data)
            response_data = {
                'store_bill': serializer.data,
                'store_items': store_items_serializer.data,
            }
            print("Store Bill =", response_data)

            return Response(response_data)
        except StoreBill.DoesNotExist:
            return Response(status=404)
        
        
class StoreAccessoriesDetailView(APIView):
    # def get(self, request, pk):
    #     try:
    #         accessories = StoreBill.objects.get(pk=pk)
    #         serializer = StoreAccessoriesSerializer(accessories)
    #         return Response(serializer.data)
    #     except StoreBill.DoesNotExist:
    #         return Response(status=404)
    
    def get(self, request, work_order):
        try:
            store = StoreBill.objects.filter(work_order__work_order=work_order).first()
            serializer = StoreAccessoriesSerializer(store)

            # Get related Store Items and serialize them
            store_items = store.storebillno.all()  # Assuming your related name is 'storeitem_set'
            store_items_serializer = StoreItemSerializer(store_items, many=True)  # You need to create storeItemSerializer
            
            print("LPLPLPLPLPLPLPLP", store_items_serializer.data)
            response_data = {
                'store_bill': serializer.data,
                'store_items': store_items_serializer.data,
            }
            print("Store Bill =", response_data)

            return Response(response_data)
        except StoreBill.DoesNotExist:
            return Response(status=404)
