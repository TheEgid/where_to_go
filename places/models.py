from django.db import models
from django.contrib.gis.db.models import PointField


class Place(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='Place')
    placeId = models.PositiveIntegerField(unique=True,blank=False)
    short_description = models.TextField(blank=True,
                                         verbose_name='Краткое описание')
    long_description = models.TextField(blank=True,
                                        verbose_name='Полное описание')
    coordinates = PointField(blank=True, null=True,
                             verbose_name='Широта и Долгота')

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['title', 'placeId', ]


class PlaceGeo(models.Model):
    title = models.CharField(verbose_name='PlaceGeo', max_length=200,
                             blank=True)
    placeId = models.CharField(unique=True, max_length=200, blank=False)
    detailsUrl = models.TextField(blank=True)
    coordinates = PointField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['title', 'placeId', ]


class Image(models.Model):
    image = models.ImageField(verbose_name='Фотография')
    location = models.ForeignKey(Place, related_name='img',
                                 on_delete=models.CASCADE, default=0)
    number = models.PositiveIntegerField(verbose_name='Позиция', null=True,
                                         blank=True, default=0)
    objects = models.Manager()

    def __str__(self):
        return f'image {str(self.number)}'

    class Meta(object):
        ordering = ['number', ]
