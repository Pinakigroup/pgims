from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Supplier

class SupplierForm(forms.ModelForm):
    supplier_name = forms.CharField(label='Supplier Name', widget=forms.TextInput(attrs={'class': 'span6 typeahead'}), required=True, error_messages={'required':'Must Enter Supplier Name'})
    company_name = forms.CharField(label="Company name", widget=forms.TextInput({'class': 'span6 typeahead', 'rows':8, 'cols':256}), required=True, error_messages={'required':'Must Enter Company name'})
    class Meta:
        model = Supplier
        fields = ['id', 'date', 'supplier_name', 'company_name', 'office_address', 'office_postal_code', 'office_country', 'office_tphone', 'factory_address', 'factory_postal_code', 'factory_country', 'factory_tphone', 'vat_identi_no', 'expiry_date', 'trade_license_no', 'owner_name', 'owner_phone', 'owner_email', 'first_cp_name', 'first_cp_position', 'first_cp_phone', 'first_cp_email', 'sec_cp_name', 'sec_cp_position', 'sec_cp_phone', 'sec_cp_email', 'account_name', 'account_no', 'bank_name', 'bank_address', 'swift']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'span6 typeahead', 'type': 'date'}),
            'office_address': forms.TextInput(attrs={'class':'span6 typeahead'}),
            'office_postal_code': forms.NumberInput(attrs={'class': 'span6 typeahead'}),
            'office_country': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'office_tphone': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            
            'factory_address': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'factory_postal_code': forms.NumberInput(attrs={'class': 'span6 typeahead'}),
            'factory_country': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'factory_tphone': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            
            'vat_identi_no': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'expiry_date': forms.TextInput(attrs={'class': 'span6 typeahead', 'type': 'date'}),
            'trade_license_no': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            
            'owner_name': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'owner_phone': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'owner_email': forms.EmailInput(attrs={'class': 'span6 typeahead'}),
            
            'first_cp_name': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'first_cp_position': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'first_cp_phone': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'first_cp_email': forms.EmailInput(attrs={'class': 'span6 typeahead'}),
            
            'sec_cp_name': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'sec_cp_position': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'sec_cp_phone': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'sec_cp_email': forms.EmailInput(attrs={'class': 'span6 typeahead'}),
            
            'account_name': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'account_no': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'bank_name': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'bank_address': forms.TextInput(attrs={'class': 'span6 typeahead'}),
            'swift': forms.TextInput(attrs={'class': 'span6 typeahead'}),
        }