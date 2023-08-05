from django.db import models
from django.utils.timezone import now

# Create your models here.


class Remarks(models.Model):
    remarks = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)  
    
    def __str__(self):
        return self.remarks