from django import forms
from django.forms import formset_factory
from .models import FabricRequisitionBill, FabricRequisitionItem, FabricRequisitionBillDetails
from stock.models import Stock
from store.models import StoreBill
from purchase_order.models import PurchaseBill
from django_select2.forms import ModelSelect2Widget
from django.contrib.auth.models import User

# form used to get customer details
class FabricRForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        # self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        # self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        # self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = FabricRequisitionBill
        fields = ['name', 'buyer_name', 'work_order_fr', 'order_no', 'fileno_po', 'card_no', 'unit', 'remarks']
        widgets = {
            'work_order_fr': ModelSelect2Widget(queryset=PurchaseBill.objects.all(), search_fields=['work_order__icontains'], attrs={'style': 'width: 100%', 'data-placeholder': 'Search Work Order No'}),
            # 'work_order_fr': ModelSelect2Widget(model=StoreBill, search_fields=['work_order__work_order__icontains'], attrs={'style': 'width: 100%', 'data-placeholder': 'Search Work Order No'}),
            'buyer_name' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'order_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'card_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'unit' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'remarks' : forms.Select(attrs = {'class' : 'textinput form-control'}),
        }
        labels = {
            'name': 'Goods Receiver',
            'buyer_name': 'Buyer Name',
            'work_order_fr': 'Work Order',
            'order_no': 'Order No',
            'fileno_po': 'File No',
            'card_no': 'Card No',
            'unit': 'Unit',
            'remarks': 'Remarks',
        }
        
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


class FabricRItemForm(forms.ModelForm):

    class Meta:
        model = FabricRequisitionItem
        fields = ['stock', 'quantity', 'uom', 'style', 'color', 'order_qty', 'cutting_qty', 'cad_consumption', 'requard_qty']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['uom'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['style'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['color'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['order_qty'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['cutting_qty'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['cad_consumption'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['requard_qty'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})

# formset used to render multiple 'FabricRequisitionItemForm'
FabricRItemFormset = formset_factory(FabricRItemForm, extra=1)

# form used to accept the other details for FabricRequisitions bill
class FabricRDetailsForm(forms.ModelForm):
    class Meta:
        model = FabricRequisitionBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']
        

# form used for search data by from date to date
class FabricRequisitionBillDateSearchForm(forms.ModelForm):                                                                     
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = FabricRequisitionBill
        fields = ['start_date', 'end_date']