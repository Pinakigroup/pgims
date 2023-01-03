from django import forms
from django.forms import formset_factory
from .models import FabricRequisitionBill, FabricRequisitionItem, FabricRequisitionBillDetails
from stock.models import Stock

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
        fields = ['name', 'buyer_name', 'po_no', 'order_no', 'card_no', 'floor', 'date', 'fabric_detail']
        widgets = {
            'buyer_name' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'po_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'order_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'card_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'floor' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'fabric_detail' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'}),
        }


class FabricRItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['unit_price'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
        self.fields['uom'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['style_no'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['fab_color'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['order_qty'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['cutting_qty'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['consumption'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['requard_qty'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = FabricRequisitionItem
        fields = ['stock', 'quantity', 'unit_price', 'uom', 'style_no', 'fab_color', 'order_qty', 'cutting_qty', 'consumption', 'requard_qty']

# formset used to render multiple 'FabricRequisitionItemForm'
FabricRItemFormset = formset_factory(FabricRItemForm, extra=1)

# form used to accept the other details for FabricRequisitions bill
class FabricRDetailsForm(forms.ModelForm):
    class Meta:
        model = FabricRequisitionBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']
