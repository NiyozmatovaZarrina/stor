from django.db import models

# Create your models here.



class Category(models.Model):
    categoryname=models.CharField("Категория", max_length=100,blank=True,null=True,default="category_default")
    
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        #ordering = ['prodaja']
         
    
    def __str__(self) -> str:
        return self.categoryname

