from django.db import models

# Create your models here.



class Prihoddetail(models.Model):
    produktname  = models.ForeignKey("produkts.produkt", on_delete=models.CASCADE, related_name="НазваниеПродукта",blank=True,null=True)
    prihod=models.ForeignKey("prihods.prihod", on_delete=models.CASCADE, related_name="Деталиприхода")
    size= models.IntegerField("Размер")  
    color=models.CharField("Цвет", max_length=100)
    price=models.FloatField("Цена", max_length=100)  
    
    
    class Meta:
        verbose_name = "ПриходДеталь"
        verbose_name_plural = "ДеталиПрихода"
        #ordering = ['prodaja']
         
     
    def __str__(self) -> str:
        return self.color

