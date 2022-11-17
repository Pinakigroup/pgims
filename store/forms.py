from pyexpat import model
from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Store

# Code

class StoreForm(forms.ModelForm):
    style = forms.CharField(label="Style", widget=forms.Textarea({'class': 'span6 typeahead', 'placeholder':'Text...', 'rows':8, 'cols':256}), required=True, error_messages={'required':'Must Enter Style'})
    class Meta:
        model = Store
        fields = ['id', 'company', 'report', 'report_no', 'report_date', 'file_no', 'lc', 'qty', 'unit_price', 'uom', 'product_item', 'buyer_name', 'style']
        widgets = {
            'company': forms.Select(attrs={'class': 'span6 typeahead'}),
            'report': forms.Select(attrs={'class': 'span6 typeahead'}),
            'report_no': forms.TextInput(attrs={'class':'span6 typeahead'}),
            'report_date': forms.TextInput(attrs={'class': 'span6 typeahead', 'type': 'date'}),
            'file_no': forms.TextInput(attrs={'class':'span6 typeahead'}),
            'lc': forms.TextInput(attrs={'class':'span6 typeahead'}),
            'qty': forms.NumberInput(attrs={'class': 'span6 typeahead'}),
            'uom': forms.Select(attrs={'class': 'span6 typeahead'}),
            'unit_price': forms.NumberInput(attrs={'class': 'span6 typeahead'}),
            'product_item': forms.Select(attrs={'class': 'span6 typeahead'}),
            'buyer_name': forms.TextInput(attrs={'class':'span6 typeahead'}),
        }
        labels = {
            'company': 'Company Name',
            'report': 'Invoice/DC',
            'report_no': 'Inv/DC No',
            'report_date': 'Inv/DC Date',
            'file_no': 'File No',
            'lc': 'LC',
            'qty': 'Qty',
            'uom': 'UOM',
            'product_item': 'Product Name',
            'buyer_name': 'Buyer Name',
            'style': 'Style',
        }