from django.db import models
from stock.models import Stock
from store.models import StoreBill
from django.utils.timezone import now
from store_receiver.models import StoreReceiver
from datetime import date

# Create your models here.


class FabricRequisitionBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    
    name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    buyer_name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    
    # work_order = models.CharField(max_length=64, blank=False, null=True)
    
    work_order_fr = models.ForeignKey(StoreBill, on_delete=models.CASCADE, blank=False, related_name='fabric_work_order')
    
    # file_no_store = models.ForeignKey(StoreBill, on_delete=models.CASCADE, blank=False, related_name='fabric_file_no')
    fileno_po = models.CharField(max_length=64, blank=False, null=True)
        
    order_no = models.CharField(max_length=32, null=True, blank=True)
    card_no = models.CharField(max_length=32, null=True, blank=True)
    FLOOR = (
        ('', 'Select'),
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
        ('5th', '5th'),
        ('6th', '6th'),
        ('7th', '7th'),
        ('8th', '8th'),
    )
    floor = models.CharField(max_length=64, null=True, blank=False, choices=FLOOR)
    date = models.DateField(default=date.today, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
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
    quantity = models.IntegerField(default=1)
    UOM = (
        ('', 'Select'),
        ('kg', 'kg'),
        ('miter', 'miter'),
        ('yard', 'yard'),
        ('pcs', 'pcs'),
        ('pound', 'pound'),
        ('g', 'g'),
        ('gg', 'gg'),
        ('litre', 'litre'),
        ('dz', 'dz'),
        ('1000 pcs', '1000 pcs'),
    )
    UNIT = (
        ('', 'Select'),
        ('miter', 'miter'),
        ('yard', 'yard'),
    )
    uom = models.CharField(max_length=64, null=True, blank=False, choices=UOM)
    unit = models.CharField(max_length=64, null=True, blank=False, choices=UNIT)
    style_no = models.CharField(max_length=64, blank=True, null=True)
    fab_color = models.CharField(max_length=64, blank=True, null=True)
    order_qty = models.IntegerField(default=0, blank=True, null=True)
    cutting_qty = models.IntegerField(default=0, blank=True, null=True)
    cad_consumption = models.CharField(max_length=64, blank=True, null=True)
    requard_qty = models.IntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    
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