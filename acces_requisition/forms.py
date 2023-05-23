from django import forms
from django.forms import formset_factory
from .models import AccesRequisitionBill, AccesRequisitionItem, AccesRequisitionBillDetails
from stock.models import Stock

# form used to get customer details
class AccesRForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        # self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        # self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        # self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = AccesRequisitionBill
        fields = ['name', 'store_receiver', 'order_no', 'style_no', 'file_no', 'line_no', 'card_no', 'date', 'supply_qty', 'remarks']
        widgets = {
            'store_receiver' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'order_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'style_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'file_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'line_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'card_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'supply_qty' : forms.NumberInput(attrs = {'class' : 'textinput form-control'}),
            'remarks' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'}),
        }
        labels = {
            'name': 'Goods Receiver',
            'store_receiver': 'Goods Issuer',
            'file_no': 'File No',
            'order_no': 'Order No',
            'style_no': 'Style No',
            'line_no': 'Line No',
            'card_no': 'Card No',
        }


class AccesRItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['uom'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['acces_color'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['size'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = AccesRequisitionItem
        fields = ['stock', 'quantity', 'uom', 'acces_color', 'size']

# formset used to render multiple 'AccesRequisitionItemForm'
AccesRItemFormset = formset_factory(AccesRItemForm, extra=1)

# form used to accept the other details for AccesRequisitions bill
class AccesRDetailsForm(forms.ModelForm):
    class Meta:
        model = AccesRequisitionBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']

# form used for search data by from date to date
class AccesRequisitionBillDateSearchForm(forms.ModelForm):                                                                     
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = AccesRequisitionBill
        fields = ['start_date', 'end_date']