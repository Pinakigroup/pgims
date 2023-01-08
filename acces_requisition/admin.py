from django.contrib import admin
from .models import AccesRequisitionBill, AccesRequisitionItem, AccesRequisitionBillDetails
# Register your models here.

admin.site.register(AccesRequisitionBill)
admin.site.register(AccesRequisitionItem)
admin.site.register(AccesRequisitionBillDetails)