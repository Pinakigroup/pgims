from datetime import date
from email.policy import default
from django.db import models
from django.utils.timezone import now
from more_itertools import first
# Create your models here. first_contP_position

class Supplier(models.Model):
    
    date = models.DateField(default= now)
    supplier_name = models.CharField(max_length=64, null=True, blank=False)
    company_name = models.CharField(max_length=64, null=True, blank=False)
    office_address = models.CharField(max_length=64, null=True, blank=True)
    office_postal_code = models.IntegerField(null=True, blank=True)
    office_country = models.CharField(max_length=64, null=True, blank=True)
    office_tphone = models.CharField(max_length=16, null=True, blank=True, unique=True)
    factory_address =  models.CharField(max_length=64, null=True, blank=True)
    factory_postal_code = models.IntegerField(null=True, blank=True)
    factory_country = models.CharField(max_length=64, null=True, blank=True)
    factory_tphone = models.CharField(max_length=16, null=True, blank=True, unique=True)
    vat_identi_no = models.CharField(max_length=32, null=True, blank=True)
    expiry_date = models.DateField(default= now, null=True, blank=True) 
    trade_license_no = models.CharField(max_length=32, null=True, blank=True)
    owner_name = models.CharField(max_length=64, null=True, blank=True)
    owner_phone = models.CharField(max_length=16, null=True, blank=True, unique=True)
    owner_email = models.EmailField(max_length=64, null=True, blank=True, unique=True)
    first_cp_name = models.CharField(max_length=64, null=True, blank=True)
    first_cp_position = models.CharField(max_length=64, null=True, blank=True)
    first_cp_phone = models.CharField(max_length=16, null=True, blank=True, unique=True)
    first_cp_email = models.EmailField(max_length=64, null=True, blank=True, unique=True)
    sec_cp_name = models.CharField(max_length=64, null=True, blank=True)
    sec_cp_position = models.CharField(max_length=64, null=True, blank=True)
    sec_cp_phone = models.CharField(max_length=16, null=True, blank=True, unique=True)
    sec_cp_email = models.EmailField(max_length=64, null=True, blank=True, unique=True)
    account_name = models.CharField(max_length=64, null=True, blank=False)
    account_no = models.CharField(max_length=32, null=True, blank=False)
    bank_name = models.CharField(max_length=64, null=True, blank=False)
    bank_address = models.CharField(max_length=64, null=True, blank= False)
    swift = models.CharField(max_length=64, null=True, blank=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.supplier_name