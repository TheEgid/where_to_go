from django.contrib.gis import admin
from django.contrib.gis.db import models as geomodels
from .widgets import LatLongWidget
from .models import Place, Image, PlaceGeo


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ('title',)

    formfield_overrides = {
        geomodels.PointField: {'widget': LatLongWidget},
    }
    inlines = [
        ImageInline,
    ]


@admin.register(PlaceGeo)
class PlaceGeoAdmin(admin.ModelAdmin):
    model = PlaceGeo
    list_display = ('title',)

    formfield_overrides = {
        geomodels.PointField: {'widget': LatLongWidget},
    }


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('title',)
