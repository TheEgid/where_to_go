from django.contrib import admin
from .models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = (
        'title', 'placeId', 'short_description', 'long_description',
        'coordinates')


