from django import forms
from .models import File

class FileForm(forms.ModelForm):
    abc = forms.ChoiceField(choices=[('deferred', 'Deferred'), ('at_sight', 'At Sight')], label='Payment Terms')
    file = forms.CharField(label='File No', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'File No'}), required=True, error_messages={'required':'Must Enter a Correct File No'})
    class Meta:
        model = File
        fields = ('file', 'buyer_name', 'abc', 'xyz', 'master_lc_sc', 'style', 'sleve', 'size_range', 'po_no', 'quantity', 'fob_rate', 'amount', 'shipment_date', 'exp_date_of_delivery')
        widgets = {
            'xyz': forms.Select(attrs={'class':'form-control'}),
            'style': forms.TextInput(attrs={'class':'form-control'}),
            'sleve': forms.TextInput(attrs={'class':'form-control'}),
            'size_range': forms.TextInput(attrs={'class':'form-control'}),
            'po_no': forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'id': 'id_quantity'}),
            'fob_rate': forms.NumberInput(attrs={'id': 'id_fob_rate'}),
            'amount': forms.NumberInput(attrs={'id': 'id_amount', 'readonly': 'readonly'}),
            'shipment_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'exp_date_of_delivery': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'xyz': 'Day',
            'fob_rate': 'FOB Rate',
            'po_no': 'PO NO',
            'buyer_name': 'Buyer Name',
            'master_lc_sc': 'MLC/SC',
            'exp_date_of_delivery': 'Expected Date of Delivery',
        }