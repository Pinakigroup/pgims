from django import forms
from django.forms import formset_factory
from .models import StoreBill, StoreItem, StoreBillDetails
from purchase_order.models import PurchaseBill
from stock.models import Stock
from django_select2.forms import ModelSelect2Widget
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# form used to get customer details
class StoreForm(forms.ModelForm):   
     
    # file_no = forms.ModelChoiceField(
    #     queryset=PurchaseBill.objects.all().order_by('file_no'),
    #     widget=ModelSelect2Widget(
    #         model=PurchaseBill,
    #         search_fields=['file_no__file__icontains'],
    #         attrs={'style': 'width: 100%'}
    #     )
    # )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
        # self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        # self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        # self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = StoreBill
        # fields = ['supplier', 'buyer_name', 'report', 'report_no', 'report_date', 'received_by', 'received_date', 'img_file', 'work_order', 'lc', 'style_no', 'file_no_wo', 'remarks', 'store_location']
        fields = '__all__'
        widgets = {
            'work_order': ModelSelect2Widget(model=PurchaseBill, search_fields=['work_order__icontains'], to_field_name="work_order", attrs={'style': 'width: 100%', 'data-placeholder': 'Search Work Order No'}),

            'report' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'report_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'report_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'fileno_po' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'master_lc_sc' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'store_location' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'remarks' : forms.Select(attrs = {'class' : 'textinput form-control'}),
        }
        labels = {
            'work_order': 'Work Order No',
            'company': 'Company',
            'buyer_name': 'Buyer Name',
            'report': 'Inv/DC',
            'report_no': 'Inv/DC No',
            'report_date': 'Inv/DC Date',
            'img_file': 'Photo',
            'po_no': 'PO No',
            'fileno_po': 'File No',
            'master_lc_sc': 'MLC/SC',
            'style_no': 'Style/Order NO',
            # 'file_no_wo': 'File No',
            'product_item': 'Product Name',
            'fabric_color': 'Fabric Color',
            'remarks': 'Remarks',
            'store_location': 'Location',
            'receive_qty': 'Receive Qty',
            'unit': 'Unit',
            'unit_price': 'Uprice',
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Name',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the default help_text
        self.fields['username'].help_text = ''
    


class StoreItemForm(forms.ModelForm):
    class Meta:
        model = StoreItem
        fields = ['stock', 'quantity', 'wo_quantity', 'received_quantity', 'unit', 'size', 'style', 'color']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['wo_quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['received_quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['unit'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['size'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['style'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['color'].widget.attrs.update({'class': 'textinput form-control'})
        

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