from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user_acc = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=64, null=True, blank=True)
    img_profile = models.ImageField(upload_to='media/profile')
    phone = models.CharField(max_length=32, null=True, blank=False, unique=True)
    designation = models.CharField("Designation", max_length=50, blank=True)
    dob = models.DateField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True) 

    def __str__(self):
        return f'{self.user_acc.username} -Profile'