from django.contrib import admin

from .models import Store

# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['company', 'report', 'report_no', 'report_date', 'file_no', 'lc', 'rec_qty', 'unit_price', 'due_qty', 'total_price', 'uom', 'product_item', 'buyer_name', 'style_no']
