from django.contrib import admin
from .models import StoreRequisition

# Register your models here.

@admin.register(StoreRequisition)
class StoreRequisitionAdmin(admin.ModelAdmin):
    list_display = ['name', 'sr_designation', 'order_no', 'style_no', 'line_no', 'card_no', 'date', 'product', 'size', 'required_qty', 'supply_qty', 'remarks']
