from django.contrib import admin
from .models import Provider

# Register your models here.

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display =["name","address","Phone_number", "Email","Website", "Activate"]
    list_filter=["name","address"]

