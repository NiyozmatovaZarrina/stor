from django.contrib import admin
from .models import Produkt

# Register your models here.

@admin.register(Produkt)
class ProduktlAdmin(admin.ModelAdmin):
    list_display =["produktname","provider","size","color","price"]
    #list_filter=["produktname","price"]