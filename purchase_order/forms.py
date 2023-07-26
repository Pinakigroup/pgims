from django import forms
from django.forms import formset_factory
from .models import PurchaseItem, PurchaseBillDetails, PurchaseBill
from file.models import File
from stock.models import Stock
from django_select2.forms import ModelSelect2Widget

class PurchaseForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        # self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = PurchaseBill
        # fields = ['supplier', 'buyer_name', 'merchandiser', 'work_order', 'po_no', 'style', 'file_no', 'sale_contact', 'po_date', 'remarks']
        fields = '__all__'
        widgets = {
            'fileno_po': ModelSelect2Widget(model=File, search_fields=['file__icontains'], attrs={'style': 'width: 100%'}),
            # 'file_no' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'merchandiser' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'po_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'style_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'work_order' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'wo_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'order_qty' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'remarks' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'})
        }
        labels = {
            'fileno_po': 'File No',
            'po_no': 'PO No',
            'work_order': 'Work Order',
            'wo_date': 'Work Order Date',
            'master_lc_sc': 'Master LC / Sales Contact',
            'style_no': 'Style/Order NO',
            'order_qty': 'Order Qty',
        }


# form used to render a single stock item form
class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['stock', 'quantity', 'unit_price', 'uom', 'size', 'style', 'color']
        
        labels = {
            'stock': 'Goods Receiver',
            'color': 'Goods Issuer',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['unit_price'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
        self.fields['uom'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['size'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['style'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['color'].widget.attrs.update({'class': 'textinput form-control'})


# formset used to render multiple 'PurchaseItemForm'
PurchaseItemFormset = formset_factory(PurchaseItemForm, extra=1)

class PurchaseDetailsForm(forms.ModelForm):
    class Meta:
        model = PurchaseBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']
        
        
# Purchase Search Form
class PurchaseSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = PurchaseBill
        fields = ['start_date', 'end_date']