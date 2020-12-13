import json
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http.response import JsonResponse
from .models import PlaceGeo, Place


def show_main(request):
    places_geojson = serializers.serialize('geojson',
                                           PlaceGeo.objects.all(),
                                           geometry_field='coordinates',
                                           fields=('title',
                                                   'placeId',
                                                   'detailsUrl'))
    return render(request=request, template_name="index.html",
                  context={"places_geojson": json.loads(places_geojson)})


def show_place(request, id):
    place = get_object_or_404(Place.objects.all(), placeId=id)

    coordinates = [coord for coord in place.coordinates]
    lng, lat = coordinates

    response_data = {
        'title': place.title,
        'imgs': [_image.image.url for _image in place.img.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {'lng': str(lng), 'lat': str(lat)},
    }

    return JsonResponse(response_data, safe=False, json_dumps_params={
        'ensure_ascii': False, 'indent': 4})
