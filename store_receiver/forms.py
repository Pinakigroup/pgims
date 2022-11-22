from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import StoreReceiver

class StoreReceiverForm(forms.ModelForm):
    name = forms.CharField(label='StoreReceiver Name', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, error_messages={'required':'Must Enter a Correct Store Receiver Name'})
    class Meta:
        model = StoreReceiver
        fields = ['id', 'name', 'designation', 'email', 'phone']
        widgets = {
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }