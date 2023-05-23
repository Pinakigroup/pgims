from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Merchandiser

class MerchandiserForm(forms.ModelForm):
    office_id = forms.CharField(label='Office Id', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, error_messages={'required':'Must Enter a Correct Office Id'})
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, error_messages={'required':'Must Enter a Correct Merchandiser Name'})
    class Meta:
        model = Merchandiser
        fields = ['id', 'office_id', 'name', 'designation', 'joining_date', 'email', 'phone', 'img', 'access_area']
        widgets = {
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'joining_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'access_area': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'img': 'Photo',
        }

class MerchandiserDateSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = Merchandiser
        fields = ['start_date', 'end_date']