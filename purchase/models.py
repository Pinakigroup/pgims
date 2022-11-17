from django.db import models
from django.utils.timezone import now
from merchandiser.models import Merchandiser
from product.models import Product
from category.models import Category
from supplier.models import Supplier

# Create your models here.

class Purchase(models.Model):
    merchandiser_name = models.ForeignKey(Merchandiser, on_delete=models.CASCADE, blank=False)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False)
    booking_qty = models.PositiveIntegerField(default=1)
    style_detail = models.TextField()
    color = models.CharField(max_length=64, null=True, blank=True)
    po_date = models.DateField(default= now)
    atten = models.CharField(max_length=64, null=True, blank=True)
    file_no = models.CharField(max_length=64, null=True, blank=True, unique=True)
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
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name 