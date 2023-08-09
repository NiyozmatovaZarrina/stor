from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):

    name = models.CharField("Название", max_length=100)
    address = models.ForeignKey("demo.author", on_delete=models.CASCADE, related_name="books")

    categories = models.ManyToManyField("demo.category", verbose_name="Категории", related_name="books")

    publish_year = models.IntegerField("Год издания")
    publisher = models.CharField("Издательство", max_length=50)
    description = models.TextField("Описание", null=True, blank=True)
    pages = models.PositiveIntegerField("Количество страниц")
    is_active = models.BooleanField("Есть в наличие", default=True)
    
    active = ActiveManager()
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
