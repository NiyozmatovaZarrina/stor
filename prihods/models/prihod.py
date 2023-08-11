from django.db import models

# Create your models here.



class Prihod(models.Model):
    provider  = models.ForeignKey("storage.provider", on_delete=models.CASCADE, related_name="Названиепоставщика")
    user=models.ForeignKey("users.user", on_delete=models.CASCADE, related_name="Пользователь")
    totalprice=models.FloatField("Цена", max_length=100)  
    
    
    class Meta:
        verbose_name = "Проход"
        verbose_name_plural = "Приходы"
        #ordering = ['prodaja']
         
    
    def __int__(self) -> int:
        return self.totalprice

