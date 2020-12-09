from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField


class Place(models.Model):
    title = models.TextField(max_length=200, blank=True, verbose_name='Place')
    placeId = models.TextField()
    short_description = models.TextField(blank=True,
                                         verbose_name='Краткое описание')
    long_description = models.TextField(blank=True,
                                        verbose_name='Полное описание')
    lat = models.FloatField('Latitude', blank=True, default=0)
    lng = models.FloatField('Longitude', blank=True, default=0)
    coordinates = PointField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.coordinates = Point(self.lng, self.lat)
        super(Place, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['title', 'placeId', ]


class Image(models.Model):
    title = models.CharField(max_length=200,
                             null=True, blank=True)
    image = models.ImageField()
    location = models.ForeignKey(Place, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.image.name
        super(Image, self).save(*args, **kwargs)

    class Meta(object):
        ordering = ['title', ]
