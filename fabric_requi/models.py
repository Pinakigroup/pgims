from django.db import models
from stock.models import Stock
from store.models import StoreBill
from remarks.models import Remarks
from django.utils.timezone import now
from store_receiver.models import StoreReceiver
from unit.models import Unit
from datetime import date
from django.utils import timezone

# Create your models here.

class FabricRequisitionBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    
    name = models.CharField(max_length=64, null=True, blank=True)
    buyer_name = models.CharField(max_length=64, null=True, blank=True)
    
    # work_order = models.CharField(max_length=64, blank=False, null=True)
    
    work_order_fr = models.ForeignKey(StoreBill, on_delete=models.CASCADE, blank=False, related_name='fabric_work_order')
    
    # file_no_store = models.ForeignKey(StoreBill, on_delete=models.CASCADE, blank=False, related_name='fabric_file_no')
    fileno_po = models.CharField(max_length=64, blank=False, null=True)
        
    order_no = models.CharField(max_length=32, null=True, blank=True)
    card_no = models.CharField(max_length=32, null=True, blank=True)
    UNIT = (
        ('', 'Select'),
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
    )
    unit = models.CharField(max_length=64, null=True, blank=False, choices=UNIT)
    date = models.DateField(auto_now_add=True, auto_now=False)
    remarks = models.ForeignKey(Remarks, on_delete=models.CASCADE, blank=False, related_name='remarksname_fabric')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return FabricRequisitionItem.objects.filter(billno=self)
        
    # def get_total_price(self):
    #     ar_items = FabricRequisitionItem.objects.filter(billno=self)
    #     total = 0
    #     for item in ar_items:
    #         total += item.totalprice
    #     return total

# contains the fabric_requisition stocks made
class FabricRequisitionItem(models.Model):
    billno = models.ForeignKey(FabricRequisitionBill, on_delete = models.CASCADE, related_name='fr_billno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='fr_item')
    # Supply QTY 
    quantity = models.DecimalField(max_digits=9, decimal_places=2)
    balance_quantity = models.DecimalField(max_digits=9, decimal_places=2)
    uom = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=False, related_name='uom_of_fabric_issue')
    style_no = models.CharField(max_length=64, blank=True, null=True)
    fab_color = models.CharField(max_length=64, blank=True, null=True)
    order_qty = models.DecimalField(max_digits=9, decimal_places=2)
    cutting_qty = models.DecimalField(max_digits=9, decimal_places=2)
    cad_consumption = models.DecimalField(max_digits=9, decimal_places=2)
    requard_qty = models.DecimalField(max_digits=9, decimal_places=2)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    
    def save(self, *args, **kwargs):
        self.balance_quantity = self.stock.quantity - self.quantity
        super(FabricRequisitionItem, self).save(*args, **kwargs)
    
# contains the other details in the fabric_requisition bill
class FabricRequisitionBillDetails(models.Model):
    billno = models.ForeignKey(FabricRequisitionBill, on_delete = models.CASCADE, related_name='fr_detailsbillno')
    
    eway = models.CharField(max_length=50, blank=True, null=True)    
    veh = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)
    
    cgst = models.CharField(max_length=50, blank=True, null=True)
    sgst = models.CharField(max_length=50, blank=True, null=True)
    igst = models.CharField(max_length=50, blank=True, null=True)
    cess = models.CharField(max_length=50, blank=True, null=True)
    tcs = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno)