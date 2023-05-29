from django import forms
from .models import File

class FileForm(forms.ModelForm):
    abc = forms.ChoiceField(choices=[('deferred', 'Deferred'), ('at_sigt', 'At Sigt')], label='Payment Terms')
    file = forms.CharField(label='File No', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'File No'}), required=True, error_messages={'required':'Must Enter a Correct File No'})
    # xyz = forms.Select(label='Field 2', required=False)
    class Meta:
        model = File
        fields = ('file', 'name', 'abc', 'xyz', 'master_lc', 'sales_contact_no', 'exp_date_of_delivery')
        widgets = {
            # 'abc': forms.Select(attrs={'class':'form-control'}),
            'name': forms.Select(attrs={'class':'form-control'}),
            'xyz': forms.Select(attrs={'class':'form-control'}),
            'master_lc': forms.TextInput(attrs={'class':'form-control'}),
            'sales_contact_no': forms.TextInput(attrs={'class':'form-control'}),
            'exp_date_of_delivery': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'xyz': 'Day',
            'name': 'Buyer Name',
            'exp_date_of_delivery': 'Expected Date of Delivery',
        }