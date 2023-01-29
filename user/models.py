from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    full_name = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField(upload_to='profile_images' ,blank=False)
    phone_no = models.CharField(max_length=16, null=True, blank=False, unique=True)
    designation = models.CharField("Designation", max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)  

    def __str__(self):
        return f'{self.user.username} Profile'
    

# def save(self, *args, **kwargs):
#     super().save(*args, **kwargs)