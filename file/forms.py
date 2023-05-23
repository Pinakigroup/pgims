from django import forms
from .models import File

class FileForm(forms.ModelForm):
    abc = forms.ChoiceField(choices=[('deferred', 'Deferred'), ('at_sigt', 'At Sigt')], label='Payment Terms')
    # xyz = forms.Select(label='Field 2', required=False)
    class Meta:
        model = File
        fields = ('file_no', 'name', 'abc', 'xyz', 'master_lc', 'sales_contact_no')
        widgets = {
            # 'abc': forms.Select(attrs={'class':'form-control'}),
            'file_no': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.Select(attrs={'class':'form-control'}),
            'xyz': forms.Select(attrs={'class':'form-control'}),
            'master_lc': forms.TextInput(attrs={'class':'form-control'}),
            'sales_contact_no': forms.TextInput(attrs={'class':'form-control'}),

        }
        labels = {
            'xyz': 'Day',
            'name': 'Buyer Name',
            'file_no': 'File NO',
        }