from django.db import models
from django.contrib.gis.db.models import PointField


class Place(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name='Place')
    placeId = models.CharField(unique=True, max_length=200, blank=False)
    short_description = models.TextField(blank=True,
                                         verbose_name='Краткое описание')
    long_description = models.TextField(blank=True,
                                        verbose_name='Полное описание')
    coordinates = PointField(blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['title', 'placeId', ]


class Image(models.Model):
    title = models.CharField(max_length=200,
                             null=True, blank=True)
    image = models.ImageField()
    location = models.ForeignKey(Place, on_delete=models.CASCADE, default=0)

    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.image.name
        super(Image, self).save(*args, **kwargs)

    class Meta(object):
        ordering = ['title', ]


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
