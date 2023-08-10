from django.db import models

# Create your models here.



class Prodaja(models.Model):
    #user  = models.ForeignKey(".user", on_delete=models.CASCADE, related_name="user")

    productname=models.CharField("Название", max_length=100)
    agentname=models.ForeignKey("agent.agent", on_delete=models.CASCADE, related_name="agent")
    totalprice= models.IntegerField("Цена")    
    
    
    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажы"
        #ordering = ['prodaja']
        
    
    def __str__(self) -> str:
        return self.productname

