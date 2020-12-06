from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField


class Place(models.Model):
    title = models.TextField(blank=True, verbose_name='Place')
    placeId = models.TextField()
    #imgs = models.CharField(max_length=200)
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    long_description = models.TextField(blank=True, verbose_name='Полное описание')
    lat = models.FloatField('Latitude', blank=True, default=0)
    lng = models.FloatField('Longitude', blank=True, default=0)
    coordinates = PointField(blank=True, null=True, srid=4326)

