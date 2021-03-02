from django.contrib.gis import admin
from django.utils.html import format_html
from django.contrib.gis.db import models as geomodels
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from .widgets import LatLongWidget
from .models import Place, Image


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Image
    autocomplete_fields = ['location', ]
    raw_id_fields = ['location', ]


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    can_delete = True
    show_change_link = True
    classes = ['collapse', ]
    readonly_fields = ['preview_image', ]
    fields = [('image', ), 'preview_image']

    def preview_image(self, obj):
        if obj:
            return format_html(
                '<img src="{image_url}" style="max-height: 250px;'
                ' max-width: 250px;/>',
                image_url=obj.image.url)
        else:
            return format_html('<b>preview image not found</b>')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ['title', ]
    search_fields = ['title', ]
    readonly_fields = ['id', ]

    formfield_overrides = {
        geomodels.PointField: {'widget': LatLongWidget},
    }
    inlines = [
        ImageInline,
    ]
