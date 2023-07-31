from django import forms
from django.db import models
from django.forms import fields, widgets
from django.contrib.auth.models import User
from .models import StoreReceiver

class StoreReceiverForm(forms.ModelForm):
    # name = forms.CharField(label='Store Receiver Name', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, error_messages={'required':'Must Enter a Correct Store Receiver Name'})
    class Meta:
        model = StoreReceiver
        # fields = ['id', 'name', 'email', 'phone', 'designation']
        fields = ['id', 'phone', 'designation']
        widgets = {
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'}),
        }
        # labels = {
        #     'name': 'Goods Receiver',
        # }
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Name',
            'email': 'Email',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the default help_text
        self.fields['username'].help_text = ''

        
class StoreReceiverDateSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = StoreReceiver
        fields = ['start_date', 'end_date']