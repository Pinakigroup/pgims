from django import forms
from django.forms import formset_factory
from .models import AccesRequisitionBill, AccesRequisitionItem, AccesRequisitionBillDetails
from stock.models import Stock
from store.models import StoreBill
from django_select2.forms import ModelSelect2Widget
from django.contrib.auth.models import User

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
        fields = ['name', 'order_no', 'acces_wo_no', 'fileno_po', 'style_no', 'line_no', 'card_no', 'date', 'supply_qty', 'remarks']
        widgets = {
            'acces_wo_no': ModelSelect2Widget(model=StoreBill, search_fields=['work_order_store__work_order__icontains'], attrs={'style': 'width: 100%'}),
            'order_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'style_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'line_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'card_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'supply_qty' : forms.NumberInput(attrs = {'class' : 'textinput form-control'}),
            'remarks' : forms.Select(attrs = {'class' : 'textinput form-control'}),
        }
        labels = {
            'name': 'Goods Receiver',
            'acces_wo_no': 'Work Order No',
            'fileno_po': 'File No',
            'order_no': 'Order No',
            'style_no': 'Style No',
            'line_no': 'Line No',
            'card_no': 'Card No',
        }
# Goods Issuer add username 
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Goods Issuer',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the default help_text
        self.fields['username'].help_text = ''


class AccesRItemForm(forms.ModelForm):
    class Meta:
        model = AccesRequisitionItem
        fields = ['stock', 'quantity', 'unit', 'acces_color', 'size', 'style']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['unit'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['acces_color'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['size'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['style'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        

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