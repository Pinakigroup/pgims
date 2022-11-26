from pyexpat import model
from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import StoreRequisition


class StoreRequisitionForm(forms.ModelForm):
    name = forms.CharField(label='StoreRequisition Name', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, error_messages={'required':'Must Enter a Correct Store Requisition Name'})
    class Meta:
        model = StoreRequisition
        fields = ['id', 'name', 'sr_designation', 'order_no', 'style_no', 'line_no', 'card_no', 'date', 'product', 'size', 'required_qty', 'supply_qty', 'remarks']
        widgets = {
            'sr_designation': forms.Select(attrs={'class':'form-control'}),
            'order_no': forms.TextInput(attrs={'class': 'form-control'}),
            'style_no': forms.TextInput(attrs={'class': 'form-control'}),
            'line_no': forms.TextInput(attrs={'class': 'form-control'}),
            'card_no': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'required_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'supply_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'sr_designation': 'Designation',
            'order_no': 'Order No',
            'style_no': 'Style No',
            'line_no': 'Line No',
            'card_no': 'Card No',
            'date': 'Date',
            'product': 'Product',
            'size': 'Size',
            'required_qty': 'Required Qty',
            'supply_qty': 'Supply Qty',
            'remarks': 'Remarks',
        }
