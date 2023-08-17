from django.contrib import admin
from .models import Prihod

# Register your models here.

@admin.register(Prihod)
class PrihodAdmin(admin.ModelAdmin):
    list_display =["user","totalprice"]
   # list_filter=[" totalprice"]
