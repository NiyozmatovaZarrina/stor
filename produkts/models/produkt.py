from django.db import models

# Create your models here.



class Produkt(models.Model):
    produktname  = models.CharField("Наименование", max_length=100,blank=True,null=True)
    provider=models.ForeignKey("storage.provider", on_delete=models.CASCADE, related_name="Провайдер")
    category =models.ForeignKey("categorys.category", on_delete=models.CASCADE, related_name="Котегори")
    size= models.IntegerField("Размер")  
    color=models.CharField("Цвет", max_length=100)
    price=models.FloatField("Цена", max_length=100)  
    
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        #ordering = ['prodaja']
         
    
    def __str__(self) -> str:
        return self.color

