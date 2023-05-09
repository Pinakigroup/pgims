from django.db import models
from stock.models import Stock
from django.utils.timezone import now
from supplier.models import Supplier
# Create your models here.

class StoreBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False, related_name='suppliername')
    buyer_name = models.CharField(max_length=64, blank=False, null=True)
    REPORT = (
        ('', 'Select'),
        ('Invoice', 'Invoice'),
        ('DC', 'DC'),
    )
    report = models.CharField(max_length=64, null=True, blank=False, choices=REPORT)
    report_no = models.CharField(max_length=64, null=True, blank=True)  
    report_date = models.DateField(default= now)
    # Sonia Kater 
    pi_no = models.CharField(max_length=150, blank=True, null=True)
    received_by = models.CharField(max_length=64, blank=False, null=True)
    received_date = models.DateField(default= now, blank=True, null=True)
    img_file = models.ImageField(upload_to='store', default='blank.png', null=True, blank=True)
    wo_no = models.CharField(max_length=64, blank=True, null=True)
    lc = models.CharField(max_length=64, blank=False, null=True)
    style_no = models.CharField(max_length=32, null=True, blank=True)
    file_no = models.CharField(max_length=64, blank=False, null=True)
    lot_no = models.CharField(max_length=64, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    store_location = models.CharField(max_length=64, blank=True, null=True)
    order_qty = models.IntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)  
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return StoreItem.objects.filter(billno=self)
        
    # def get_total_price(self):
    #     storeitems = StoreItem.objects.filter(billno=self)
    #     total = 0
    #     for item in storeitems:
    #         total += item.totalprice
    #     return total
    
class StoreItem(models.Model):
    billno = models.ForeignKey(StoreBill, on_delete = models.CASCADE, related_name='storebillno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='storeitem')
    quantity = models.IntegerField(default=1)
    fabric_color = models.CharField(max_length=64, blank=True, null=True)
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
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    
class StoreBillDetails(models.Model):
    billno = models.ForeignKey(StoreBill, on_delete = models.CASCADE, related_name='storedetailsbillno')
    
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