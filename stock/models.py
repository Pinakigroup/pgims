from django.db import models
from category.models import Category
from unit.models import Unit

# Create your models here.

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.DecimalField(max_digits=9, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=False, related_name='unit_of_stocks')
    
    is_deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name