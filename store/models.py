from django.db import models
from django.utils.timezone import now
from product.models import Product
from supplier.models import Supplier
from purchase.models import Purchase

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
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    rec_qty = models.PositiveIntegerField(default=1)
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
    unit_price = models.FloatField()
    total_price=models.FloatField(editable=False, default=0)
    due_qty = models.PositiveIntegerField(default=0)
    buyer_name = models.CharField(max_length=64, blank=False, null=True)
    style_no = models.CharField(max_length=32, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.company.company_name
    
    def save(self,*args, **kwargs):
        self.total_price = self.rec_qty * self.unit_price
        super(Store, self).save(*args, **kwargs)   

    # def save(self,*args, **kwargs):
    #     self.due_qty = self.id.booking_qty - self.rec_qty
    #     super(Store, self).save(*args, **kwargs)          