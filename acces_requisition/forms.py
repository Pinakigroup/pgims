from django import forms
from django.forms import formset_factory
from .models import AccesRequisitionBill, AccesRequisitionItem, AccesRequisitionBillDetails
from stock.models import Stock
from store.models import StoreBill
from purchase_order.models import PurchaseBill
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
        fields = ['name', 'acces_wo_no', 'fileno_po', 'style_no', 'po_no', 'unit_no', 'card_no', 'remarks']
        widgets = {
            # 'acces_wo_no': ModelSelect2Widget(queryset=PurchaseBill.objects.all(), search_fields=['work_order__icontains'], attrs={'style': 'width: 100%', 'data-placeholder': 'Search Work Order No'}),
            'acces_wo_no': ModelSelect2Widget(model=StoreBill, search_fields=['work_order__work_order__icontains'], attrs={'style': 'width: 100%', 'data-placeholder': 'Search Work Order No'}),
            'style_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'po_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'unit_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'card_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'remarks' : forms.Select(attrs = {'class' : 'textinput form-control'}),
        }
        labels = {
            'name': 'Goods Receiver',
            'acces_wo_no': 'Work Order No',
            'fileno_po': 'File No',
            'style_no': 'Style/Order No',
            'unit_no': 'Unit No',
            'card_no': 'Card No',
            'po_no': 'PO No',
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
        fields = ['stock', 'quantity', 'unit', 'color', 'size', 'style']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        
        stock_quantity = Stock.objects.first()  # Get the first Stock instance
        placeholder = stock_quantity.quantity if stock_quantity else 'Enter quantity'
        self.fields['quantity'].widget.attrs['placeholder'] = placeholder
            
        # self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['unit'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['color'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['size'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['style'].widget.attrs.update({'class': 'textinput form-control'})
        
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