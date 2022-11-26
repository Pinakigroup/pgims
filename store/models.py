from django.db import models
from django.forms import CharField
from django.utils.timezone import now
from purchase.models import Purchase
from product.models import Product
from supplier.models import Supplier

# Create your models here.
class Store(models.Model):
    company = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False)
    REPORT = (
        ('', 'Select'),
        ('Invoice', 'Invoice'),
        ('DC', 'DC'),
    )
    report = models.CharField(max_length=64, null=True, blank=False, choices=REPORT)
    report_no = models.CharField(max_length=64, blank=False, null=True)
    report_date = models.DateField(default= now)
    file_no = models.CharField(max_length=64, blank=False, null=True)
    lc = models.CharField(max_length=64, blank=False, null=True)
    qty = models.PositiveIntegerField(default=1)
    unit_price = models.FloatField()
    total_price=models.FloatField(editable=False, default=0)
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
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    buyer_name = models.CharField(max_length=64, blank=False, null=True)
    style_no = models.CharField(max_length=32, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.company
    
    def save(self,*args, **kwargs):
        self.total_price = self.qty * self.unit_price
        super(Store, self).save(*args, **kwargs)    