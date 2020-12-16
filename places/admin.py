from django.contrib.gis import admin
from django.utils.html import format_html
from django.contrib.gis.db import models as geomodels
from adminsortable2.admin import SortableInlineAdminMixin
from .widgets import LatLongWidget
from .models import Place, Image, PlaceGeo


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image


@admin.register(PlaceGeo)
class PlaceGeoAdmin(admin.ModelAdmin):
    model = PlaceGeo
    list_display = ('title',)

    formfield_overrides = {
        geomodels.PointField: {'widget': LatLongWidget},
    }


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    can_delete = True
    show_change_link = True
    classes = ('collapse',)
    readonly_fields = ('preview_image',)
    fields = (('image', ), 'preview_image')

    def preview_image(self, obj):
        width = obj.image.width
        height = obj.image.height
        MAX_SIZE = 99
        if width > height:
            resized_width = MAX_SIZE
            resized_height = int(
                round((MAX_SIZE / float(width)) * height))
        else:
            resized_height = MAX_SIZE
            resized_width = int(
                round((MAX_SIZE / float(height)) * width))
        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=resized_width,
                height=resized_height,
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ('title',)
    readonly_fields = ('placeId',)

    formfield_overrides = {
        geomodels.PointField: {'widget': LatLongWidget},
    }
    inlines = [
        ImageInline,
    ]
