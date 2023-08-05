from django import forms
from django.db import models
from django.forms import fields, Widget
from .models import Remarks

class RemarksForm(forms.ModelForm):
    class Meta:
        model = Remarks
        fields = ['id', 'remarks']
        widgets = {
            'remarks' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'})
        }
        

class RemarksDateSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = Remarks
        fields = ['start_date', 'end_date']