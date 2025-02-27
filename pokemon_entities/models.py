# from django.contrib.gis.gdal.prototypes.raster import auto_create_warped_vrt
from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
