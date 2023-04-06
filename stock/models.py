from django.db import models
from category. models import Category
# Create your models here.

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
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
    is_deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)  

    def __str__(self):
        return self.name