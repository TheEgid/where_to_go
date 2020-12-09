from django.contrib import admin
from .models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('title',)


