from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Supplier

class SupplierForm(forms.ModelForm):
    supplier_name = forms.CharField(label='Supplier/Company Name', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, error_messages={'required':'Must Enter Supplier Name'})
    class Meta:
        model = Supplier
        fields = ['id', 'date', 'supplier_name', 'office_address', 'office_postal_code', 'office_country', 'office_tphone', 'factory_address', 'factory_postal_code', 'factory_country', 'factory_tphone', 'vat_identi_no', 'expiry_date', 'trade_license_no', 'owner_name', 'owner_phone', 'owner_email', 'first_cp_name', 'first_cp_position', 'first_cp_phone', 'first_cp_email', 'sec_cp_name', 'sec_cp_position', 'sec_cp_phone', 'sec_cp_email', 'account_name', 'account_no', 'bank_name', 'bank_address', 'swift']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'office_address': forms.TextInput(attrs={'class':'form-control'}),
            'office_postal_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'office_country': forms.TextInput(attrs={'class': 'form-control'}),
            'office_tphone': forms.TextInput(attrs={'class': 'form-control'}),
            
            'factory_address': forms.TextInput(attrs={'class': 'form-control'}),
            'factory_postal_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'factory_country': forms.TextInput(attrs={'class': 'form-control'}),
            'factory_tphone': forms.TextInput(attrs={'class': 'form-control'}),
            
            'vat_identi_no': forms.TextInput(attrs={'class': 'form-control'}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trade_license_no': forms.TextInput(attrs={'class': 'form-control'}),
            
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_email': forms.EmailInput(attrs={'class': 'form-control'}),
            
            'first_cp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_cp_position': forms.TextInput(attrs={'class': 'form-control'}),
            'first_cp_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'first_cp_email': forms.EmailInput(attrs={'class': 'form-control'}),
            
            'sec_cp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sec_cp_position': forms.TextInput(attrs={'class': 'form-control'}),
            'sec_cp_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'sec_cp_email': forms.EmailInput(attrs={'class': 'form-control'}),
            
            'account_name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_no': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_address': forms.TextInput(attrs={'class': 'form-control'}),
            'swift': forms.TextInput(attrs={'class': 'form-control'}),
        }


        labels = {
            'office_address': 'Address',
            'office_postal_code': 'Postal Code',
            'office_country': 'Country',
            'office_tphone': 'Tphone No',
            
            'factory_address': 'Address',
            'factory_postal_code': 'Postal Code',
            'factory_country': 'Country',
            'factory_tphone': 'Tphone No',
            
            'vat_identi_no': 'Vat Identification No',
            'expiry_date': 'Expiry Date',
            'trade_license_no': 'Trade License No',
            
            'owner_name': 'Name',
            'owner_phone': 'Contact No',
            'owner_email': 'Email',
            
            'first_cp_name': 'Name',
            'first_cp_position': 'Position',
            'first_cp_phone': 'Contact No',
            'first_cp_email': 'Email',
            
            'sec_cp_name': 'Name',
            'sec_cp_position': 'Position',
            'sec_cp_phone': 'Contact No',
            'sec_cp_email': 'Email',
            
            'account_name': 'Account Name',
            'account_no': 'Account No',
            'bank_name': 'Bank Name',
            'bank_address': 'Bank Address',   
            'swift': 'SWIFT',           
        }

class SupplierDateSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = Supplier
        fields = ['start_date', 'end_date']