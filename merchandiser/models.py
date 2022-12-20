from django.db import models
from django.utils.timezone import now
# Create your models here.


class Merchandiser(models.Model):
    office_id = models.CharField(max_length=64, null=True, blank=True, unique=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    designation = models.CharField(max_length=64, null=True, blank=True)
    joining_date = models.DateField(default= now) 
    email = models.EmailField(max_length=64, blank=True, unique=True)
    phone = models.CharField(max_length=16, null=True, blank=True, unique=True)
    access_area = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)  
    
    def __str__(self):
        return self.name