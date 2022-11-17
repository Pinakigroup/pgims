from django import forms
from django.db import models
from django.forms import ModelForm, fields, widgets
from .models import Purchase 

class PurchaseForm(forms.ModelForm):
    style_detail = forms.CharField(label="Style Detail", widget=forms.Textarea({'class': 'span6 typeahead', 'placeholder':'Text...', 'rows':8, 'cols':256}), required=True, error_messages={'required':'Must Enter Style Detail'})
    class Meta:
        model = Purchase
        fields = ['id', 'merchandiser_name', 'product_name', 'category_name', 'supplier_name', 'booking_qty', 'style_detail', 'color', 'po_date', 'atten', 'file_no', 'uom']
        widgets = {
            'merchandiser_name': forms.Select(attrs={'class': 'span6 typeahead'}),
            'product_name': forms.Select(attrs={'class': 'span6 typeahead'}),
            'category_name': forms.Select(attrs={'class': 'span6 typeahead'}),
            'supplier_name': forms.Select(attrs={'class': 'span6 typeahead'}),
            'booking_qty': forms.NumberInput(attrs={'class': 'span6 typeahead'}),
            # 'style_detail': forms.Textarea(attrs={'class': 'span6 typeahead', 'placeholder':'Style Detail', 'rows':8, 'cols':256}, required=True, error_messages={'required':'Must Enter Descriptions'}),
            'color': forms.TextInput(attrs={'class':'span6 typeahead'}),
            'po_date': forms.TextInput(attrs={'class': 'span6 typeahead', 'type': 'date'}),
            'atten': forms.TextInput(attrs={'class':'span6 typeahead'}),
            'file_no': forms.TextInput(attrs={'class':'span6 typeahead'}),
            'uom': forms.Select(attrs={'class': 'span6 typeahead'}),
        }