from django.db import models
from stock.models import Stock
from store.models import StoreBill
from django.utils.timezone import now
from store_receiver.models import StoreReceiver

# Create your models here.


#contains the acces_requisition bills made
class AccesRequisitionBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=64, null=True, blank=True)
    store_receiver = models.ForeignKey(StoreReceiver, on_delete=models.CASCADE, blank=False)
    order_no = models.CharField(max_length=32, null=True, blank=True)
    style_no = models.CharField(max_length=32, null=True, blank=True)
    file_no_ar = models.ForeignKey(StoreBill, on_delete=models.CASCADE, blank=False, related_name='Acces_file_no')
    line_no = models.CharField(max_length=32, null=True, blank=True)
    card_no = models.CharField(max_length=32, null=True, blank=True)
    date = models.DateField(default= now, null=True, blank=True)
    supply_qty = models.PositiveIntegerField(default=1, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
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
    quantity = models.IntegerField(default=1, blank=True, null=True)
    UOM = (
        ('', 'Select'),
        ('kg', 'kg'),
        ('miter', 'miter'),
        ('yard', 'yard'),
        ('pcs', 'pcs'),
        ('pound', 'pound'),
        ('cone', 'cone'),
        ('g', 'g'),
        ('gg', 'gg'),
        ('litre', 'litre'),
        ('dg', 'dg'),
        ('1000 pcs', '1000 pcs'),
    )
    uom = models.CharField(max_length=64, null=True, blank=False, choices=UOM)
    acces_color = models.CharField(max_length=64, blank=True, null=True)
    size = models.CharField(max_length=64, null=True, unique=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    
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
