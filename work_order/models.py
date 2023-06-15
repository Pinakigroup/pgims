from django.db import models
from django.utils.timezone import now
# from supplier.models import Supplier
# from stock.models import Stock
from purchase_order.models import PurchaseBill
# from merchandiser.models import Merchandiser
from datetime import date
import datetime
import random

# Create your models here.

# def generate_random_number():
#     return random.randint(100, 999)

class WorkOrderBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False, related_name='suppliersname')
    # buyer_name = models.CharField(max_length=64, blank=False, null=True)
    # merchandiser = models.ForeignKey(Merchandiser, on_delete=models.CASCADE, blank=False, related_name='merchandisersname')
    
    f_no = models.ForeignKey(PurchaseBill, on_delete=models.CASCADE, related_name='wo_file_no')
    style_no = models.CharField(max_length=32, null=True, blank=True)
    work_order = models.CharField(max_length=64, blank=False, null=True)
    # work_order = models.CharField(max_length=64, default=generate_random_number)
    

    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    # def __str__(self):
    #     return "Bill no: " + str(self.file_no)
    
    def __str__(self):
        return str(self.f_no.fileno_po.file)

    # def get_items_list(self):
    #     return WorkOrderItem.objects.filter(billno=self)

    # def get_total_price(self):
    #     work_orderitems = WorkOrderItem.objects.filter(billno=self)
    #     total = 0
    #     for item in work_orderitems:
    #         total = total + item.totalprice
    #     return total
    
    # Generate a uniq no
    # def wo_no(self):               
    #     ymdt = str(self.created_at)
    #     ymd = ymdt[:10]
    #     rep = ymd.replace("-", "")
    #     po = rep[2:]
    #     p = "AGD"+ po + str(self.work_order)
    #     return p
    
# #contains the work_order stocks made
# class WorkOrderItem(models.Model):
#     billno = models.ForeignKey(WorkOrderBill, on_delete = models.CASCADE, related_name='work_orderbillno')
#     stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='work_orderitem')
#     quantity = models.IntegerField(default=1, null=True, blank=True)
#     unit_price = models.IntegerField(default=1, null=True, blank=True)
#     totalprice = models.IntegerField(default=1, null=True, blank=True)
#     UOM = (
#         ('', 'Select'),
#         ('kg', 'kg'),
#         ('miter', 'miter'),
#         ('yard', 'yard'),
#         ('pcs', 'pcs'),
#         ('pound', 'pound'),
#         ('g', 'g'),
#         ('gg', 'gg'),
#         ('litre', 'litre'),
#         ('dg', 'dg'),
#         ('1000 pcs', '1000 pcs'),
#     )
#     uom = models.CharField(max_length=64, null=True, blank=True, choices=UOM)
#     size = models.CharField(max_length=64, null=True, blank=True)
#     style_no = models.CharField(max_length=64, blank=True, null=True)
#     color = models.CharField(max_length=64, blank=True, null=True)
    
#     updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    

#     def __str__(self):
#         return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    
    

# class  WorkOrderBillDetails(models.Model):
#     billno = models.ForeignKey(WorkOrderBill, on_delete = models.CASCADE, related_name=' work_orderdetailsbillno')
    
#     eway = models.CharField(max_length=50, blank=True, null=True)    
#     veh = models.CharField(max_length=50, blank=True, null=True)
#     destination = models.CharField(max_length=50, blank=True, null=True)
#     po = models.CharField(max_length=50, blank=True, null=True)
    
#     cgst = models.CharField(max_length=50, blank=True, null=True)
#     sgst = models.CharField(max_length=50, blank=True, null=True)
#     igst = models.CharField(max_length=50, blank=True, null=True)
#     cess = models.CharField(max_length=50, blank=True, null=True)
#     tcs = models.CharField(max_length=50, blank=True, null=True)
#     total = models.CharField(max_length=50, blank=True, null=True)
#     updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

#     def __str__(self):
#         return "Bill no: " + str(self.billno.billno)