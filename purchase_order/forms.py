from django import forms
from django.forms import formset_factory
from .models import PurchaseItem, PurchaseBillDetails, PurchaseBill
from stock.models import Stock

class PurchaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        # self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = PurchaseBill
        fields = ['supplier', 'merchandiser', 'work_order', 'po_no', 'file_no', 'po_date', 'detail']
        widgets = {
            'merchandiser' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'work_order' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'po_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'file_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'po_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'detail' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'})
        }


# form used to render a single stock item form
class PurchaseItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['unit_price'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
        self.fields['uom'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['size'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['style_no'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['color'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = PurchaseItem
        fields = ['stock', 'quantity', 'unit_price', 'uom', 'size', 'style_no', 'color']

# formset used to render multiple 'PurchaseItemForm'
PurchaseItemFormset = formset_factory(PurchaseItemForm, extra=1)

class PurchaseDetailsForm(forms.ModelForm):
    class Meta:
        model = PurchaseBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']