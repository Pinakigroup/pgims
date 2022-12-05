from django.db import models
from django.utils.timezone import now
from store_receiver.models import StoreReceiver
from product.models import Product

# Create your models here.

class FabricRequisition(models.Model):
    name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    srf_designation = models.ForeignKey(StoreReceiver, on_delete=models.CASCADE, blank=False)
    buyer_name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    po_no = models.CharField(max_length=32, null=True, blank=True)
    order_no = models.CharField(max_length=32, null=True, blank=True)
    style_no = models.CharField(max_length=32, null=True, blank=True)
    card_no = models.CharField(max_length=32, null=True, blank=True)
    colour = models.CharField(max_length=64, null=True, unique=True, blank=True)
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    order_qty = models.PositiveIntegerField(default=1)
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
    cutting_qty = models.CharField(max_length=64, null=True, unique=True, blank=True)
    consumption = models.CharField(max_length=64, null=True, unique=True, blank=True)
    req_qty = models.CharField(max_length=64, null=True, unique=True, blank=True)
    supply_qty = models.CharField(max_length=64, null=True, unique=True, blank=True)
    remarks = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name