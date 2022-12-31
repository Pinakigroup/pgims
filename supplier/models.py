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
    office_address = models.CharField(max_length=64, null=True, blank=False)
    # office_city = models.CharField(max_length=64, null=True, blank=False)
    office_postal_code = models.IntegerField()
    office_country = models.CharField(max_length=64, null=True, blank=False)
    office_tphone = models.CharField(max_length=16, null=True, blank=False, unique=True)
    factory_address =  models.CharField(max_length=64, null=True, blank=False)
    # factory_city = models.CharField(max_length=64, null=True, blank=False)
    factory_postal_code = models.IntegerField()
    factory_country = models.CharField(max_length=64, null=True, blank=False)
    factory_tphone = models.CharField(max_length=16, null=True, blank=False, unique=True)
    vat_identi_no = models.CharField(max_length=32, blank=False)
    expiry_date = models.DateField(default= now) 
    trade_license_no = models.CharField(max_length=32, blank=False)
    owner_name = models.CharField(max_length=64, null=True, blank=False)
    owner_phone = models.CharField(max_length=16, null=True, blank=False, unique=True)
    owner_email = models.EmailField(max_length=64, blank=False, unique=True)
    
    first_cp_name = models.CharField(max_length=64, null=True, blank=False)
    first_cp_position = models.CharField(max_length=64, null=True, blank=False)
    first_cp_phone = models.CharField(max_length=16, null=True, blank=False, unique=True)
    first_cp_email = models.EmailField(max_length=64, blank=False, unique=True)
    
    sec_cp_name = models.CharField(max_length=64, null=True, blank=False)
    sec_cp_position = models.CharField(max_length=64, null=True, blank=False)
    sec_cp_phone = models.CharField(max_length=16, null=True, blank=False, unique=True)
    sec_cp_email = models.EmailField(max_length=64, blank=False, unique=True)
    
    account_name = models.CharField(max_length=64, null=True, blank=False)
    account_no = models.CharField(max_length=32, null=True, blank=False)
    bank_name = models.CharField(max_length=64, null=True, blank=False)
    bank_address = models.CharField(max_length=64, null=True, blank= False)
    swift = models.CharField(max_length=64, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)  
    
    def __str__(self):
        return self.supplier_name