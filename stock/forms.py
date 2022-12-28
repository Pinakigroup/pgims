from mimetypes import init
from dataclasses import fields
from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                          # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
    class Meta:
        model = Stock
        fields = ['category', 'name', 'quantity']
        
        