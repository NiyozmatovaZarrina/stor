from django.db import models

# Create your models here.


class User(models.Model):

    username = models.CharField("Название", max_length=100)
    #password = models.IntegerField()
    Email = models.CharField("Email", max_length=50)
    
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    
    def __str__(self) -> str:
        return self.username
