from django.contrib import admin
from .models import Remarks

# Register your models here.

@admin.register(Remarks)
class RemarksAdmin(admin.ModelAdmin):
    list_display = ['remarks']