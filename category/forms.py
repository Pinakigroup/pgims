from django import forms
from django.db import models
from django.forms import fields, Widget
from .models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Category Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Category Name'}), required=True, error_messages={'required':'Must Enter a Correct Name'})
    class Meta:
        model = Category
        fields = ['id', 'name']
        widgets = {
            'created_at': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
                
class CategoryDateSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = Category
        fields = ['start_date', 'end_date']