from django.db import models
from django.contrib.gis.db.models import PointField
from tinymce import models as tinymce_models


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400, verbose_name='Место')
    short_description = models.TextField(blank=True,
                                         verbose_name='Краткое описание')
    long_description = tinymce_models.HTMLField(blank=True,
                                                verbose_name='Полное описание')
    coordinates = PointField(blank=True,
                             null=True,
                             verbose_name='Широта и Долгота')
    detailsUrl = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'id', ]


class Image(models.Model):
    image = models.ImageField(verbose_name='Фотография')
    location = models.ForeignKey(Place,
                                 related_name='images',
                                 verbose_name='Место',
                                 on_delete=models.CASCADE)
    number = models.PositiveIntegerField(verbose_name='Позиция', default=0)

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['number', ]
