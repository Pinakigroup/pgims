from pyexpat import model
from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Store

# Code

class StoreForm(forms.ModelForm):
    style_no = forms.CharField(label="Style No", widget=forms.TextInput({'class': 'form-control', 'rows':8, 'cols':256}), required=True, error_messages={'required':'Must Enter Style'})
    class Meta:
        model = Store
        fields = ['id', 'company', 'report', 'report_no', 'report_date', 'file_no', 'lc', 'rec_qty', 'due_qty', 'unit_price', 'uom', 'product_item', 'buyer_name', 'style_no']
        widgets = {
            'company': forms.Select(attrs={'class': 'form-control'}),
            'report': forms.Select(attrs={'class': 'form-control'}),
            'report_no': forms.TextInput(attrs={'class':'form-control'}),
            'report_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'file_no': forms.TextInput(attrs={'class':'form-control'}),
            'lc': forms.TextInput(attrs={'class':'form-control'}),
            'rec_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'uom': forms.Select(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'due_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_item': forms.Select(attrs={'class': 'form-control'}),
            'buyer_name': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'company': 'Company Name',
            'report': 'Invoice/DC',
            'report_no': 'Inv/DC No',
            'report_date': 'Inv/DC Date',
            'file_no': 'File No',
            'lc': 'LC',
            'rec_qty': 'Receive Qty',
            'due_qty': 'Due Qty',
            'unit_price': 'Unit Price',
            'uom': 'UOM',
            'product_item': 'Product Name',
            'buyer_name': 'Buyer Name',
        }