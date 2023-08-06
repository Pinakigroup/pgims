from django import forms
from django.db import models
from django.forms import fields, Widget
from .models import Unit

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['id', 'unit']
        widgets = {
            'unit': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'unit': 'Unit',
        }

class UnitDateSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = Unit
        fields = ['start_date', 'end_date']