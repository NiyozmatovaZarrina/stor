from django.db import models

# Create your models here.



class Prodajadetail(models.Model):
    produktname  = models.ForeignKey("produkts.produkt", on_delete=models.CASCADE, related_name="Название")
    prihod=models.ForeignKey("prodaja.prodaja", on_delete=models.CASCADE, related_name="prodaja")
    size= models.IntegerField("Размер")  
    color=models.CharField("Цвет", max_length=100)
    price=models.FloatField("Цена", max_length=100)  
    
    
    class Meta:
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"
        #ordering = ['prodaja']
         
    
    def __str__(self) -> str:
        return self.produktname

