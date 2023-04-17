from django import forms
from django.forms import formset_factory
from .models import StoreBill, StoreItem, StoreBillDetails
from stock.models import Stock

# form used to get customer details
class StoreForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
        # self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        # self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        # self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = StoreBill
        fields = ['supplier', 'buyer_name', 'report', 'report_no', 'report_date', 'pi_no', 'received_by', 'received_date', 'img_file', 'po_no', 'lc', 'style_no', 'file_no', 'lot_no', 'fabric_detail', 'store_location', 'order_qty']
        widgets = {
            
            'buyer_name' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'report' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'report_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'report_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'pi_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'received_by' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'received_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            
            'po_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'lc' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'style_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'file_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'lot_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'order_qty' : forms.NumberInput(attrs = {'class' : 'textinput form-control'}),
            'fabric_detail' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'}),
            'store_location' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
        }
        labels = {
            'company': 'Company',
            'buyer_name': 'Buyer Name',
            'report': 'Inv/DC',
            'report_no': 'Inv/DC No',
            'report_date': 'Inv/DC Date',
            'pi_no': 'PI',
            'received_by': 'Received By',
            'received_date': 'Received Date',
            'img_file': 'Photo',
            
            'po_no': 'PO',
            'lc': 'LC',
            'style_no': 'Style No',
            'file_no': 'File No',
            'lot_no': 'Lot No',
            'product_item': 'Product Name',
            'fabric_color': 'Fabric Color',
            'fabric_detail': 'Fabric Detail',
            'store_location': 'Location',
            'order_qty': 'Order Qty',
            'receive_qty': 'Receive Qty',
            'uom': 'UOM',
            'unit_price': 'Uprice',
        }


class StoreItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'false'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'false'})
        self.fields['uom'].widget.attrs.update({'class': 'textinput form-control', 'required': 'false'})
        self.fields['fabric_color'].widget.attrs.update({'class': 'textinput form-control', 'required': 'false'})
    class Meta:
        model = StoreItem
        fields = ['stock', 'quantity', 'uom', 'fabric_color']

# formset used to render multiple 'StoreItemForm'
StoreItemFormset = formset_factory(StoreItemForm, extra=1)


# form used to accept the other details for Store bill
class StoreDetailsForm(forms.ModelForm):
    class Meta:
        model = StoreBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']


class StockSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = StoreBill
        fields = ['start_date', 'end_date']