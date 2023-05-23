from django import forms
from django.db import models
from django.forms import fields, Widget
from .models import Buyer

class BuyerForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Buyer Name'}), required=True, error_messages={'required':'Must Enter a Correct Name'})
    class Meta:
        model = Buyer
        fields = ['id', 'name', 'address', 'country', 'type']
        widgets = {
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}), 
            'type' : forms.Select(attrs = {'class' : 'textinput form-control'}),
        }
        
class BuyerDateSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = Buyer
        fields = ['start_date', 'end_date']