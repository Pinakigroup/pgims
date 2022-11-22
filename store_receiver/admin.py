from django.contrib import admin
from .models import StoreReceiver

# Register your models here.

@admin.register(StoreReceiver)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'email', 'phone']