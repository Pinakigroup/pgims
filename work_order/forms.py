from django import forms
from .models import WorkOrderBill
from purchase_order.models import PurchaseBill
from django.forms import fields, Widget
from django_select2.forms import ModelSelect2Widget

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrderBill
        fields = ['f_no', 'style_no', 'work_order']
        widgets = {
            'f_no': ModelSelect2Widget(model=PurchaseBill, search_fields=['fileno_po__file__icontains'], attrs={'style': 'width: 100%'})
        }