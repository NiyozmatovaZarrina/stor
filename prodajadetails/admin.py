from django.contrib import admin
from .models import Prodajadetail

# Register your models here.

@admin.register(Prodajadetail)
class ProdajadetailAdmin(admin.ModelAdmin):
    list_display =["prihod","size","color","price"]
    #list_filter=[" username","email"]



