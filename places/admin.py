from django.contrib.gis import admin
from django.utils.html import format_html
from django.contrib.gis.db import models as geomodels
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from .widgets import LatLongWidget
from .models import Place, Image, PlaceGeo
from .utils import resize_sides


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
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
        if obj:
            width, height = resize_sides(obj.image.width, obj.image.height)
            return format_html(f'<img src="{obj.image.url}" '
                               f'width="{width}" height={height} />')
        else:
            return format_html("No Preview")


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

