from django.contrib import admin
from .models import Supplier

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['date', 'supplier_name', 'office_address', 'office_postal_code', 'office_country', 'office_tphone', 'factory_address', 'factory_postal_code', 'factory_country', 'factory_tphone', 'vat_identi_no', 'expiry_date', 'trade_license_no', 'owner_name', 'owner_phone', 'owner_email', 'first_cp_name', 'first_cp_position', 'first_cp_phone', 'first_cp_email', 'sec_cp_name', 'sec_cp_position', 'sec_cp_phone', 'sec_cp_email', 'account_name', 'account_no', 'bank_name', 'bank_address', 'swift']
