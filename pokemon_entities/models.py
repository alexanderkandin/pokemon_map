# from django.contrib.gis.gdal.prototypes.raster import auto_create_warped_vrt
from tkinter.constants import CASCADE

from django.db import models  # noqa F401
from django.db.models import ForeignKey


class Pokemon(models.Model):
    title = models.CharField("Имя на русском", max_length=200)
    title_en = models.CharField("Имя на английском",max_length=200,blank=True,default="Unknown")
    title_jp = models.CharField("Имя на японском",max_length=200,blank=True,default="Unknown")
    description = models.TextField("Описание",blank=True,default="")
    img = models.ImageField("Изображение",upload_to='image/', blank=True, null=True, default='default.jpg')
    previous_evolution = models.ForeignKey("self",on_delete=models.CASCADE,null=True, blank=True, related_name='next_evolutions',verbose_name="Следующая эволюция")
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
        blank=True,
        default=0
    )
    lon = models.FloatField(
        "Долгота",
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
    level = models.PositiveSmallIntegerField(
        "Уровень",
        blank=True,
        null=True
    )
    health = models.PositiveSmallIntegerField(
        "Здоровье",
        blank=True,
        null=True
    )
    strength = models.PositiveSmallIntegerField(
        "Сила",
        blank=True,
        null=True
    )
    defence = models.PositiveSmallIntegerField(
        "Защита",
        blank=True,
        null=True
    )
    stamina = models.PositiveSmallIntegerField(
        "Выносливость",
        blank=True,
        null=True
    )


    def __str__(self):
        return f"{self.pokemon.title} at {self.lat}, {self.lon}"