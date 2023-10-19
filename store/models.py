from django.db import models
from stock.models import Stock
from django.utils.timezone import now
from supplier.models import Supplier
from remarks.models import Remarks
from purchase_order.models import PurchaseBill
from store_receiver.models import StoreReceiver
from unit.models import Unit
from datetime import date

# Create your models here.

class StoreBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)

    supplier = models.CharField(max_length=64, blank=False, null=True)
    buyer_name = models.CharField(max_length=64, blank=False, null=True)
    REPORT = (
        ('', 'Doc.Select'),
        ('Invoice', 'Invoice'),
        ('DC', 'DC'),
    )
    report = models.CharField(max_length=64, null=True, blank=False, choices=REPORT)
    report_no = models.CharField(max_length=64, null=True, blank=True)
    report_date = models.DateField(default=date.today, null=True, blank=True)
    # Sonia Kater 
    
    received_date = models.DateField(auto_now_add=True, auto_now=False)
    img_file = models.ImageField(upload_to='store', default='blank.png', null=True, blank=True)
    work_order = models.ForeignKey(PurchaseBill, on_delete=models.CASCADE, blank=False, related_name='store_file_no')
    
    master_lc_sc = models.CharField(max_length=64, blank=False, null=True)
    style_no = models.CharField(max_length=32, null=True, blank=True)
    fileno_po = models.CharField(max_length=64, blank=False, null=True)
    store_location = models.CharField(max_length=64, blank=True, null=True)
    remarks = models.ForeignKey(Remarks, on_delete=models.CASCADE, blank=False, related_name='remarksname_store')
    
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)  
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.work_order.work_order)
    
    # def __str__(self):
    #     return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return StoreItem.objects.filter(billno=self)
        
    # def get_stock_qty(self):
    #     storeitems = StoreItem.objects.filter(billno=self)
    #     total = 0
    #     for item in storeitems:
    #         total += item.stock_qty
    #     return totalca
    
class StoreItem(models.Model):
    billno = models.ForeignKey(StoreBill, on_delete = models.CASCADE, related_name='storebillno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='storeitem')
    wo_quantity = models.DecimalField(max_digits=12, decimal_places=2)
    
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    balance_quantity = models.DecimalField(max_digits=12, decimal_places=2)
    
    today_received_quantity = models.DecimalField(max_digits=12, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=False, related_name='unit_of_store')
    size = models.CharField(max_length=64, null=True, blank=True)
    style = models.CharField(max_length=64, blank=True, null=True)
    color = models.CharField(max_length=64, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name

    def save(self, *args, **kwargs):
        self.balance_quantity = self.stock.quantity + self.quantity
        super(StoreItem, self).save(*args, **kwargs)
    
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