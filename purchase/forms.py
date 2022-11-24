from django import forms
from django.db import models
from django.forms import ModelForm, fields, widgets
from .models import Purchase 

class PurchaseForm(forms.ModelForm):
    style_detail = forms.CharField(label="Style Detail", widget=forms.Textarea({'class': 'form-control', 'placeholder':'Text...', 'rows':8, 'cols':256}), required=True, error_messages={'required':'Must Enter Style Detail'})
    class Meta:
        model = Purchase
        fields = ['id', 'merchandiser_name', 'product_name', 'category_name', 'supplier_name', 'booking_qty', 'style_detail', 'color', 'po_date', 'atten', 'file_no', 'uom']
        widgets = {
            'merchandiser_name': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.Select(attrs={'class': 'form-control'}),
            'category_name': forms.Select(attrs={'class': 'form-control'}),
            'supplier_name': forms.Select(attrs={'class': 'form-control'}),
            'booking_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'style_detail': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Style Detail', 'rows':8, 'cols':256}, required=True, error_messages={'required':'Must Enter Descriptions'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'po_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'atten': forms.TextInput(attrs={'class':'form-control'}),
            'file_no': forms.TextInput(attrs={'class':'form-control'}),
            'uom': forms.Select(attrs={'class': 'form-control'}),
        }