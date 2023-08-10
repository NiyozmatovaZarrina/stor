from django.db import models

# Create your models here.



class Agent(models.Model):

    clientname = models.CharField("Название", max_length=100)
    address = models.CharField("Адрес", max_length=100)
    clientphone = models.IntegerField("Телефон")
    
    
    class Meta:
        verbose_name = "Агент"
        verbose_name_plural = "Агенты"
        
    
    def __str__(self) -> str:
        return self.clientname
