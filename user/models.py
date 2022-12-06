from django.db import models
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField(upload_to='profile_images' ,blank=False)
    email = models.EmailField(max_length=64, blank=True, unique=True)
    phone_no = models.CharField(max_length=16, null=True, blank=False, unique=True)
    city = models.CharField("City", max_length=50, blank=True)
    designation = models.CharField("Designation", max_length=50, blank=True)
    country = models.CharField("Country", max_length=50, blank=True)

def __str__(self):
    return f'{self.user.username} Profile'

# def save(self, *args, **kwargs):
#     super().save(*args, **kwargs)