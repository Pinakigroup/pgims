from django.contrib import admin
from .models import PurchaseBill, PurchaseItem, PurchaseBillDetails
# Register your models here.

# admin.site.register(PurchaseBill)
# admin.site.register(PurchaseItem)
admin.site.register(PurchaseBillDetails)


@admin.register(PurchaseBill)
class PurchaseBillAdmin(admin.ModelAdmin):
    list_display = ('work_order', 'supplier', 'po_no', 'remarks', 'created_at')
    list_filter = ('supplier', 'remarks', 'created_at')
    search_fields = ('work_order', 'po_no', 'buyer_name')

@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('billno', 'stock', 'quantity', 'unit_price', 'totalprice', 'unit', 'size', 'style', 'color', 'created_at')
    list_filter = ('billno__supplier', 'stock', 'unit')
    search_fields = ('billno__work_order', 'stock__name', 'style', 'color')
