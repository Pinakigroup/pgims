from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, error_messages={'required':'Must Enter a Correct Name'})
    description = forms.CharField(label="Description", widget=forms.Textarea({'class': 'form-control', 'placeholder':'Text ...', 'rows':8, 'cols':256}), required=True, error_messages={'required':'Must Enter Descriptions'})
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }