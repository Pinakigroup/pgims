from django.db import models
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64, null=True, unique=True, blank=True)
    created_at = models.DateField(default= now) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name