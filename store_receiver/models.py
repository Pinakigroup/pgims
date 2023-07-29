from django.db import models
from django.utils.timezone import now

# Create your models here.

class StoreReceiver(models.Model):
    # name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    # email = models.EmailField(max_length=64, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=16, null=True, blank=True, unique=True)
    designation = models.CharField(max_length=64, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False) 
    
    def __str__(self):
        return self.name