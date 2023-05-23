from django.db import models
from django.utils.timezone import now
from supplier.models import Supplier
from merchandiser.models import Merchandiser
from stock.models import Stock
import datetime
from datetime import date
import random

# Create your models here.


def generate_random_number():
    return random.randint(100, 999)

#contains the purchase bills made
class PurchaseBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False, related_name='suppliersname')
    buyer_name = models.CharField(max_length=64, blank=False, null=True)
    merchandiser = models.ForeignKey(Merchandiser, on_delete=models.CASCADE, blank=False, related_name='merchandisersname')
    po_no = models.CharField(max_length=32, null=True, blank=True)
    style = models.CharField(max_length=32, null=True, blank=True)
    wo_date = models.DateField(default= now, null=True, blank=True)
    
    work_order = models.IntegerField(default=generate_random_number)
    # po_id = models.CharField(max_length=32, null=True, blank=False)
    file_no = models.CharField(max_length=64, null=True, blank=False)
    sale_contact = models.CharField(max_length=64, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return PurchaseItem.objects.filter(billno=self)

    def get_total_price(self):
        purchaseitems = PurchaseItem.objects.filter(billno=self)
        total = 0
        for item in purchaseitems:
            total = total + item.totalprice
        return total
    
    # Generate a uniq no
    def wo_no(self):               
        ymdt = str(self.created_at)
        ymd = ymdt[:10]
        rep = ymd.replace("-", "")
        po = rep[2:]
        p = "AGD"+ po + str(self.work_order)
        return p
    

#contains the purchase stocks made
class PurchaseItem(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete = models.CASCADE, related_name='purchasebillno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='purchaseitem')
    quantity = models.IntegerField(default=1, null=True, blank=True)
    unit_price = models.IntegerField(default=1, null=True, blank=True)
    totalprice = models.IntegerField(default=1, null=True, blank=True)
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
    uom = models.CharField(max_length=64, null=True, blank=True, choices=UOM)
    size = models.CharField(max_length=64, null=True, blank=True)
    style_no = models.CharField(max_length=64, blank=True, null=True)
    color = models.CharField(max_length=64, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    
    
#contains the other details in the purchases bill
class PurchaseBillDetails(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete = models.CASCADE, related_name='purchasedetailsbillno')
    
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