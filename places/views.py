import json
from django.http.response import JsonResponse
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .utils import clear_string
from .models import PlaceGeo, Place


def show_main(request):
    geo_places_queryset = PlaceGeo.objects.all()

    for geo_place in geo_places_queryset:
        detail_url = reverse(show_place, kwargs={'id': geo_place.id})
        geo_place.detailsUrl = detail_url

    places_geojson = serializers.serialize('geojson',
                                           geo_places_queryset,
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
        'description_short': clear_string(place.short_description),
        'description_long': clear_string(place.long_description),
        'coordinates': {'lng': str(lng), 'lat': str(lat)},
    }

    return JsonResponse(response_data, safe=False, json_dumps_params={
        'ensure_ascii': False, 'indent': 4})
