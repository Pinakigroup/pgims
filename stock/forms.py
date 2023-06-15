from mimetypes import init
from dataclasses import fields
from django import forms
from .models import Stock
from category.models import Category
from django_select2.forms import ModelSelect2Widget

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                          # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
    class Meta:
        model = Stock
        fields = ['category', 'name', 'quantity', 'uom']
        widgets = {
            'category': ModelSelect2Widget(model=Category, search_fields=['name__icontains'], attrs={'style': 'width: 100%'}),
            'uom' : forms.Select(attrs = {'class' : 'textinput form-control'}),
        }
        labels = {
            'uom': 'Unit',
        }
        
class StockDateSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = Stock
        fields = ['start_date', 'end_date']