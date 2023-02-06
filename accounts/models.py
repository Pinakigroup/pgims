from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="profile")
    full_name = models.CharField(max_length=64, null=True, blank=True)
    img_profile = models.ImageField(upload_to='profile', default='default.png', null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True, unique=True)
    designation = models.CharField("Designation", max_length=50, null=True, blank=True)
    dob = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True) 
    
    def __str__(self):
        return f'{self.user.username} -Profile'