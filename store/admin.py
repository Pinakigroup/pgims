from django.contrib import admin

from .models import Store

# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['company', 'buyer_name', 'report', 'report_no', 'report_date', 'po_no', 'lc', 'style_no', 'file_no', 'lot_no', 'product_item', 'fabric_color', 'fabric_detail', 'store_location', 'order_qty', 'receive_qty', 'uom', 'unit_price']
