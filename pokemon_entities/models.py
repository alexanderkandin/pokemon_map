# from django.contrib.gis.gdal.prototypes.raster import auto_create_warped_vrt
from tkinter.constants import CASCADE

from django.db import models  # noqa F401
from django.db.models import ForeignKey


class Pokemon(models.Model):
    title = models.CharField("Имя на русском", max_length=200)
    title_en = models.CharField("Имя на английском",max_length=200,default="Unknown")
    title_jp = models.CharField("Имя на японском",max_length=200,default="Unknown")
    description = models.TextField("Описание",blank=True,null=True)
    img_url = models.ImageField("Изображение",upload_to='image/', blank=True, null=True, default='default.jpg')
    next_evolution = models.ForeignKey("self",on_delete=models.CASCADE,null=True, blank=True, related_name='previous',verbose_name="Следующая эволюция")
    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name="entities",
        verbose_name="Покемон"
    )
    lat = models.FloatField(
        "Широта",
        null=True,
        blank=True,
        default=0
    )
    lon = models.FloatField(
        "Долгота",
        null=True,
        blank=True,
        default=0
    )
    appearance_at = models.DateTimeField(
        "Время появления",
        null=True,
        blank=True
    )
    disappeared_at = models.DateTimeField(
        "Время исчезновения",
        null=True,
        blank=True
    )
    level = models.IntegerField(
        "Уровень",
        default=0
    )
    health = models.IntegerField(
        "Здоровье",
        default=0
    )
    strength = models.IntegerField(
        "Сила",
        default=0
    )
    defence = models.IntegerField(
        "Защита",
        default=0
    )
    stamina = models.IntegerField(
        "Выносливость",
        default=0
    )


    def __str__(self):
        return f"{self.pokemon.title} at {self.lat}, {self.lon}"