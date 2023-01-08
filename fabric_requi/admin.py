from django.contrib import admin
from .models import FabricRequisitionBill, FabricRequisitionItem, FabricRequisitionBillDetails
# Register your models here.

admin.site.register(FabricRequisitionBill)
admin.site.register(FabricRequisitionItem)
admin.site.register(FabricRequisitionBillDetails)