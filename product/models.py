from django.db import models
from django.utils import timezone
from category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.name