from django.db import models

# Create your models here.

class User(models.Model):


    username=models.CharField("Имя", max_length=100)
    email=models.EmailField("Email", max_length=254)
    password= models.IntegerField("Пароль")    
    
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
         
    
    def __str__(self) -> str:
        return self.username

