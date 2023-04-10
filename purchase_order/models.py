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
    work_order = models.CharField(max_length=32, null=True, blank=True)
    po_date = models.DateField(default= now)
    
    po_id = models.IntegerField(default=generate_random_number)
    # po_no = models.CharField(max_length=32, null=True, blank=False)
    file_no = models.CharField(max_length=64, null=True, blank=True, unique=True)
    detail = models.TextField()
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
    def po_no(self):               
        today = date.today()
        ymd = str(today.year), str(today.month), str(today.day)
        ymds = ymd[0] + ymd[1] + ymd[2]
        po = ymds[2:]
        p = "AGD"+ po + str(self.po_id)
        return p
    
    

#contains the purchase stocks made
class PurchaseItem(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete = models.CASCADE, related_name='purchasebillno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='purchaseitem')
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