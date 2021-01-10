from django.contrib.gis import admin
from django.utils.html import format_html
from django.contrib.gis.db import models as geomodels
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from .widgets import LatLongWidget
from .models import Place, Image


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    can_delete = True
    show_change_link = True
    classes = ['collapse', ]
    readonly_fields = ['preview_image', ]
    fields = [('image', ), 'preview_image']

    def preview_image(self, obj):
        img_width = '99px'
        if obj:
            return format_html(f'<img src="{obj.image.url}" '
                               f'alt="Preview" style="width:{img_width}">')
        else:
            return format_html("No Preview")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ['title', ]
    readonly_fields = ['placeId', ]

    formfield_overrides = {
        geomodels.PointField: {'widget': LatLongWidget},
    }
    inlines = [
        ImageInline,
    ]
