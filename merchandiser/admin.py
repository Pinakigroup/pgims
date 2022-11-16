from django.contrib import admin
from .models import Merchandiser

# Register your models here.
@admin.register(Merchandiser)
class MerchandiserAdmin(admin.ModelAdmin):
    list_display = ['office_id', 'name', 'designation', 'joining_date', 'email', 'phone', 'access_area']
