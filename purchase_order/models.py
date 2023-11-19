from django.db import models
from django.utils.timezone import now
from supplier.models import Supplier
from merchandiser.models import Merchandiser
from remarks.models import Remarks
from unit.models import Unit
from file.models import File
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
    po_no = models.CharField(max_length=32, null=True, blank=True)
    fileno_po = models.ForeignKey(File, on_delete=models.CASCADE, blank=False, related_name='fileno_pos')
    style_no = models.CharField(max_length=32, null=True, blank=True)
    work_order = models.CharField(max_length=64, default=generate_random_number)
    wo_date = models.DateField(auto_now_add=True, auto_now=False)
    master_lc_sc = models.CharField(max_length=64, null=True, blank=True)
    remarks = models.ForeignKey(Remarks, on_delete=models.CASCADE, blank=False, related_name='remarksname')
    
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    # def __str__(self):
    #     return "Bill no: " + str(self.file_no)
    
    def __str__(self):
        return str(self.work_order)

    def get_items_list(self):
        return PurchaseItem.objects.filter(billno=self)

    def get_total_price(self):
        purchaseitems = PurchaseItem.objects.filter(billno=self)
        total = 0
        for item in purchaseitems:
            total = total + item.totalprice
        return total
    
    # Generate a uniq no
    # def wo_no(self):               
    #     ymdt = str(self.created_at)
    #     ymd = ymdt[:10]
    #     rep = ymd.replace("-", "")
    #     po = rep[2:]
    #     p = "AGD"+ po
    #     return p
    
    # Generate a uniq no 
    # def wo_no(self):               
    #     ymdt = str(self.created_at)
    #     ymd = ymdt[:10]
    #     rep = ymd.replace("-", "")
    #     po = rep[2:]
    #     p = "AGD" + po + str(self.work_order)
    #     lp = p.replace("ne", "")
    #     return lp
    
    def wo_no(self):               
        ymdt = str(self.created_at)
        ymd = ymdt[:10]
        rep = ymd.replace("-", "")
        po = rep[2:]
        p = "AGD"+ po + str(self.work_order)
        lp = p.replace("ne", "")
        return lp

    def create_work_order(self):
        today = datetime.datetime.today().date()
        year = str(today.year)[2:]
        month = str(today.month)
        last_obj = PurchaseBill.objects.last().order_by('-created_at')
        if last_obj:
            order_number = int(last_obj.work_order[-4:]) + 1
        else:
            order_number = PurchaseBill.objects.all().count() + 1
        count = '{0}'.format(str(order_number).zfill(3))
        month = '{0}'.format(str(month).zfill(2))
        return f"{year}{month}{count}"
    
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only generate 'p' if the instance is being created
            # self.work_order = self.create_work_order()
            self.work_order = generate_random_number()
        super().save(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     if not self.pk:  # Only generate 'p' value for new instances
    #         ymdt = str(self.created_at)
    #         ymd = ymdt[:10]
    #         rep = ymd.replace("-", "")
    #         po = rep[2:]
    #         print("po:", self.created_at)
    #         # self.work_order = "AGD" + po + str(self.work_order)
    #         l = "AGD" + po + str(self.work_order)
    #         lp = l.replace("ne", "")
    #         self.work_order = lp
    #     super().save(*args, **kwargs)



#contains the purchase stocks made
class PurchaseItem(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete = models.CASCADE, related_name='purchasebillno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='purchaseitem')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    totalprice = models.DecimalField(max_digits=12, decimal_places=2)    
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=False, related_name='unit_of_wos')
    size = models.CharField(max_length=64, blank=True, null=True)
    style = models.CharField(max_length=64, blank=True, null=True)
    color = models.CharField(max_length=64, blank=True, null=True)
    
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.billno.work_order)
    
    # def __str__(self):
    #     return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    
    
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