from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import FabricRequisition


class FabricRequisitionForm(forms.ModelForm):
    name = forms.CharField(label='FabricRequisition Name', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, error_messages={'required':'Must Enter a Correct Fabric Requisition Name'})
    class Meta:
        model = FabricRequisition
        fields = ['id', 'name', 'srf_designation', 'buyer_name', 'po_no', 'order_no', 'style_no', 'card_no', 'colour', 'floor', 'date', 'product', 'order_qty', 'uom', 'cutting_qty', 'consumption', 'req_qty', 'supply_qty', 'remarks']
        widgets = {
            'srf_designation': forms.Select(attrs={'class':'form-control'}),
            'buyer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'po_no': forms.TextInput(attrs={'class': 'form-control'}),
            'order_no': forms.TextInput(attrs={'class': 'form-control'}),
            'style_no': forms.TextInput(attrs={'class': 'form-control'}),
            'card_no': forms.TextInput(attrs={'class': 'form-control'}),
            'colour': forms.TextInput(attrs={'class': 'form-control'}),
            'floor': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
                        
            'order_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'uom': forms.Select(attrs={'class': 'form-control'}),
            
            'cutting_qty': forms.TextInput(attrs={'class': 'form-control'}),
            'consumption': forms.TextInput(attrs={'class': 'form-control'}),
            'req_qty': forms.TextInput(attrs={'class': 'form-control'}),
            'supply_qty': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'srf_designation': 'Designation',
            'buyer_name': 'Buyer Name',
            'po_no': 'PO No',
            'order_no': 'Order No',
            'style_no': 'Style No',
            'card_no': 'Card No',
            'colour': 'Colour',
            'floor': 'Floor',
            'date': 'Date',
            'product': 'Product',
            'order_qty': 'Order Qty',
            'uom': 'UOM',
            'cutting_qty': 'Cutting Qty',
            'consumption': 'Consumption',
            'req_qty': 'Req Qty',
            'supply_qty': 'Supply Qty',
            'remarks': 'Remarks',
        }
