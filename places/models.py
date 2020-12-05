from django.db import models
from django.contrib.gis.db.models import PointField


class Place(models.Model):
    title = models.TextField()
    placeId = models.TextField()
    #imgs = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    coordinates = PointField()
