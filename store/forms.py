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
        fields = ['id', 'company', 'buyer_name', 'report', 'report_no', 'report_date', 'po_no', 'lc', 'style_no', 'file_no', 'lot_no', 'product_item', 'fabric_color', 'fabric_detail', 'store_location', 'order_qty', 'receive_qty', 'uom', 'unit_price']
        widgets = {
            'company': forms.Select(attrs={'class': 'form-control'}),
            'buyer_name': forms.TextInput(attrs={'class':'form-control'}),
            'report': forms.Select(attrs={'class': 'form-control'}),
            'report_no': forms.TextInput(attrs={'class':'form-control'}),
            'report_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'po_no': forms.TextInput(attrs={'class':'form-control'}),
            'lc': forms.TextInput(attrs={'class':'form-control'}),
            'style_no': forms.TextInput(attrs={'class':'form-control'}),
            'file_no': forms.TextInput(attrs={'class':'form-control'}),
            'lot_no': forms.TextInput(attrs={'class':'form-control'}),
            'product_item': forms.Select(attrs={'class': 'form-control'}),
            'fabric_color': forms.TextInput(attrs={'class':'form-control'}),
            'fabric_detail': forms.Textarea(attrs={'class':'form-control'}),
            'store_location': forms.TextInput(attrs={'class':'form-control'}),
            'order_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'receive_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'uom': forms.Select(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
        labels = {
            'company': 'Company',
            'buyer_name': 'Buyer Name',
            'report': 'Inv/DC',
            'report_no': 'Inv/DC No',
            'report_date': 'Inv/DC Date',
            'po_no': 'PO No',
            'lc': 'LC',
            'style_no': 'Style No',
            'file_no': 'File No',
            'lot_no': 'Lot No',
            'product_item': 'Product Name',
            'fabric_color': 'Fabric Color',
            'fabric_detail': 'Fabric Detail',
            'store_location': 'Location',
            'order_qty': 'Order Qty',
            'receive_qty': 'Receive Qty',
            'uom': 'UOM',
            'unit_price': 'Uprice',
        }