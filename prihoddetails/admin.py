from django.contrib import admin
from .models import Prihoddetail

# Register your models here.

@admin.register(Prihoddetail)
class PrihoddetailAdmin(admin.ModelAdmin):
    list_display =["produktname","prihod","size","color","price"]
   # list_filter=[" totalprice"]



