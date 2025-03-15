# from django.contrib.gis.gdal.prototypes.raster import auto_create_warped_vrt
from tkinter.constants import CASCADE

from django.db import models  # noqa F401
from django.db.models import ForeignKey


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200,default="Unknown")
    title_jp = models.CharField(max_length=200,default="Unknown")
    description = models.TextField(blank=True,null=True)

    img_url = models.ImageField(upload_to='image/', blank=True, null=True, default='default.jpg')
    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="entities")
    lat = models.FloatField(null=True, blank=True,default=0)
    lon = models.FloatField(null=True, blank=True,default=0)
    appearance_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    stregth = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.pokemon.title} at {self.lat}, {self.lon}"