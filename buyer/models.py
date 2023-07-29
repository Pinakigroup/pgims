from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    TYPE = (
        ('', 'Select'),
        ('direct_customer', 'Direct Customer'),
        ('buying_house', 'Buying House'),
    )
    type = models.CharField(max_length=64, null=True, blank=False, choices=TYPE)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)  
    
    def __str__(self):
        return self.name