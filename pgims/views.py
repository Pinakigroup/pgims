from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from category.models import Category
from product.models import Product
from supplier.models import Supplier
from merchandiser.models import Merchandiser
from purchase.models import Purchase
from store.models import Store
from accounts.decorators import allowed_users

# Create your views here.

@login_required
@allowed_users(allowed_roles=['admin'])
def home(request):
    total_category = Category.objects.count()
    total_product = Product.objects.count()
    total_merchandiser = Merchandiser.objects.count()
    total_supplier = Supplier.objects.count()
    total_purchase = Purchase.objects.count()
    total_store = Store.objects.count()
    stores = Store.objects.all().order_by('-id')
    
    context = {
        'name': total_category,
        'description': total_product,
        'office_id': total_merchandiser,
        'supplier_name': total_supplier,
        'style_detail': total_purchase,
        'style': total_store,
        'stores': stores
    }
    return render(request, 'home.html', context)
