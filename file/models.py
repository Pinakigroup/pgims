from django.db import models
from buyer.models import Buyer
from django.utils.timezone import now
# Create your models here.

class File(models.Model):
    file = models.CharField(max_length=64, null=True, blank=False)
    name = models.ForeignKey(Buyer, on_delete=models.CASCADE, blank=False, related_name='buyersname')
    master_lc = models.CharField(max_length=128, null=True, blank=True)
    sales_contact_no = models.CharField(max_length=128, null=True, blank=True)
    abc = models.CharField(max_length=50)
    DAY = (
        ('', 'Select'),
        ('30 day', '30 day'),
        ('45 day', '45 day'),
        ('60 day', '60 day'),
        ('75 day', '75 day'),
        ('90 day', '90 day'),
        ('105 day', '105 day'),
        ('120 day', '120 day'),
    )
    xyz = models.CharField(max_length=64, null=True, blank=True, choices=DAY)
    # expected date of delivery 
    exp_date_of_delivery = models.DateField(default= now, null=True, blank=True) 
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)  
    
    def __str__(self):
        return str(self.file)