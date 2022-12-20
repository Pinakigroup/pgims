from django.db import models
from django.utils.timezone import now
from store_receiver.models import StoreReceiver
from product.models import Product

# Create your models here.

class StoreRequisition(models.Model):
    name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    sr_designation = models.ForeignKey(StoreReceiver, on_delete=models.CASCADE, blank=False)
    order_no = models.CharField(max_length=32, null=True, blank=True)
    style_no = models.CharField(max_length=32, null=True, blank=True)
    line_no = models.CharField(max_length=32, null=True, blank=True)
    card_no = models.CharField(max_length=32, null=True, blank=True)
    date = models.DateField(default= now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    SIZE = (
        ('', 'Select'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    size = models.CharField(max_length=64, null=True, blank=False, choices=SIZE)
    required_qty = models.PositiveIntegerField(default=1)
    supply_qty = models.PositiveIntegerField(default=1)
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)  
    
    def __str__(self):
        return self.name
    


    # def __str__(self):
    #     return "Bill no: " + str(self.billno)

    # def get_items_list(self):
    #     return SaleItem.objects.filter(billno=self)
        
    # def get_total_price(self):
    #     saleitems = SaleItem.objects.filter(billno=self)
    #     total = 0
    #     for item in saleitems:
    #         total += item.totalprice
    #     return total