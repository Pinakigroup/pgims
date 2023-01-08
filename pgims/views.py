from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from category.models import Category
from supplier.models import Supplier
from merchandiser.models import Merchandiser
from purchase_order.models import PurchaseItem
from stock.models import Stock
from store.models import StoreBill, StoreItem
from accounts.decorators import allowed_users, admin_only

# Create your views here.

@login_required
@admin_only
@allowed_users(allowed_roles=['admin', 'merchandiser'])
def home(request):
    total_category = Category.objects.count()
    total_merchandiser = Merchandiser.objects.count()
    total_supplier = Supplier.objects.count()
    total_store = StoreBill.objects.count()
    total_purchase = PurchaseItem.objects.count()
    total_stock = Stock.objects.count()
    stocks = Stock.objects.all().order_by('-id')
    
    context = {
        'name': total_category,
        'office_id': total_merchandiser,
        'supplier_name': total_supplier,
        'stock': total_purchase,
        'billno': total_store,
        'billno': total_stock,
        'stocks': stocks
    }
    return render(request, 'home.html', context)
