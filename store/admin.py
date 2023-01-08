from django.contrib import admin
from .models import StoreBill, StoreItem, StoreBillDetails
# Register your models here.

admin.site.register(StoreBill)
admin.site.register(StoreItem)
admin.site.register(StoreBillDetails)