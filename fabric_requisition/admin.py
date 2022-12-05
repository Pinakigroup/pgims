from django.contrib import admin
from .models import FabricRequisition

# Register your models here.


@admin.register(FabricRequisition)
class FabricRequisitionAdmin(admin.ModelAdmin):
    list_display = ['name', 'srf_designation', 'buyer_name', 'po_no', 'order_no', 'style_no', 'card_no', 'colour', 'floor', 'date', 'product', 'order_qty', 'uom', 'cutting_qty', 'consumption', 'req_qty', 'supply_qty', 'remarks']