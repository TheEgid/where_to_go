from django.shortcuts import render
import json
from django.core import serializers
from .models import PlaceGeo


def show_main(request):
    places_geojson = serializers.serialize('geojson',
                                           PlaceGeo.objects.all(),
                                           geometry_field='coordinates',
                                           fields=('title',
                                                   'placeId',
                                                   'detailsUrl'))
    return render(request=request, template_name="index.html",
                  context={"places_geojson": json.loads(places_geojson)})

