from django.db import models
from stock.models import Stock
from django.utils.timezone import now


# Create your models here.


class FabricRequisitionBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    
    name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    # srf_designation = models.ForeignKey(StoreReceiver, on_delete=models.CASCADE, blank=False)
    buyer_name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    po_no = models.CharField(max_length=32, null=True, blank=True)
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
    date = models.DateField(default= now)
    fabric_detail = models.TextField()

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return FabricRequisitionItem.objects.filter(billno=self)
        
    def get_total_price(self):
        ar_items = FabricRequisitionItem.objects.filter(billno=self)
        total = 0
        for item in ar_items:
            total += item.totalprice
        return total

# contains the fabric_requisition stocks made
class FabricRequisitionItem(models.Model):
    billno = models.ForeignKey(FabricRequisitionBill, on_delete = models.CASCADE, related_name='fr_billno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='fr_item')
    # Supply QTY 
    quantity = models.IntegerField(default=1)
    unit_price = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)
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
        ('dg', 'dg'),
        ('1000 pcs', '1000 pcs'),
    )
    uom = models.CharField(max_length=64, null=True, blank=False, choices=UOM)
    style_no = models.CharField(max_length=64, blank=True, null=True)
    fab_color = models.CharField(max_length=64, blank=True, null=True)
    order_qty = models.IntegerField(default=0)
    cutting_qty = models.IntegerField(default=0)
    consumption = models.IntegerField(default=0)
    requard_qty = models.IntegerField(default=0)

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

    def __str__(self):
        return "Bill no: " + str(self.billno.billno)