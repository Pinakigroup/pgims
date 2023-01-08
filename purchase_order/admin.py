from django.contrib import admin
from .models import PurchaseBill, PurchaseItem, PurchaseBillDetails
# Register your models here.

admin.site.register(PurchaseBill)
admin.site.register(PurchaseItem)
admin.site.register(PurchaseBillDetails)