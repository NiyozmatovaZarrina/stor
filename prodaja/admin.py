from django.contrib import admin
from .models import Prodaja

# Register your models here.

@admin.register(Prodaja)
class ProdajaAdmin(admin.ModelAdmin):
    list_display =["username","productname","agentname","totalprice"]
   # list_filter=[" totalprice"]



