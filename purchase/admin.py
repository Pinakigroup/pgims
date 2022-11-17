import imp
from django.contrib import admin
from .models import Purchase
# Register your models here.

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['merchandiser_name', 'product_name', 'category_name', 'supplier_name', 'booking_qty', 'style_detail', 'color', 'po_date', 'atten', 'file_no', 'uom']