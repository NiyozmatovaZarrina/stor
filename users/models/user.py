from django.db import models

# Create your models here.



class User(models.Model):

    username = models.CharField("Имя", max_length=100)
    password = models.CharField("Проль", max_length=100)
    Email = models.EmailField("Email", max_length=50)
    
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    
    def __str__(self) -> str:
        return self.name
