from django.db import models
from stock.models import Stock
from store.models import StoreBill
from django.utils.timezone import now
from remarks.models import Remarks
from store_receiver.models import StoreReceiver
from datetime import date
from unit.models import Unit

# Create your models here.


#contains the acces_requisition bills made
class AccesRequisitionBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    style_no = models.CharField(max_length=32, null=True, blank=True)
    acces_wo_no = models.ForeignKey(StoreBill, on_delete=models.CASCADE, blank=False, related_name='acces_wo_no')
    fileno_po = models.CharField(max_length=64, blank=False, null=True)
    po_no = models.CharField(max_length=64, blank=False, null=True)
    unit_no = models.CharField(max_length=32, null=True, blank=True)
    card_no = models.CharField(max_length=32, null=True, blank=True)
    date = models.DateField(auto_now_add=True, auto_now=False)
    remarks = models.ForeignKey(Remarks, on_delete=models.CASCADE, blank=False, related_name='remarksname_acces')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return AccesRequisitionItem.objects.filter(billno=self)
    
        

# contains the acces_requisition stocks made
class AccesRequisitionItem(models.Model):
    billno = models.ForeignKey(AccesRequisitionBill, on_delete = models.CASCADE, related_name='ar_billno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='ar_item')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    balance_quantity = models.DecimalField(max_digits=12, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=False, related_name='unit_of_a_issue')
    color = models.CharField(max_length=64, blank=True, null=True)
    size = models.CharField(max_length=64, null=True, blank=True)
    style = models.CharField(max_length=64, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name

    # def get_balance_quantity(self):
    #     return self.stock.quantity - self.sales_quantity
    
    def save(self, *args, **kwargs):
        self.balance_quantity = self.stock.quantity - self.quantity
        super(AccesRequisitionItem, self).save(*args, **kwargs)
    
# contains the other details in the acces_requisition bill
class AccesRequisitionBillDetails(models.Model):
    billno = models.ForeignKey(AccesRequisitionBill, on_delete = models.CASCADE, related_name='ar_detailsbillno')
    
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
