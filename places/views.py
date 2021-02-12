from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from .models import Place


def show_main(request):
    geo_places_queryset = Place.objects.all()
    places_geojson = {"type": "FeatureCollection", "features": []}

    for geo_place in geo_places_queryset:
        detail_url = reverse(show_place, kwargs={'id': geo_place.placeId})
        lng, lat = geo_place.coordinates.coords
        places_geojson['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lng, lat]
                },
                "properties": {
                    "title": geo_place.title,
                    "placeId": geo_place.placeId,
                    "detailsUrl": detail_url
                }
            }
        )
    return render(request, template_name="index.html",
                  context={"places_geojson": places_geojson})


def show_place(request, id):
    place = get_object_or_404(Place.objects.all(), placeId=id)
    lng, lat = place.coordinates

    response_data = {
        'title': place.title,
        'imgs': [_image.image.url for _image in place.img.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {'lng': lng, 'lat': lat},
    }

    return JsonResponse(response_data, safe=False, json_dumps_params={
        'ensure_ascii': False, 'indent': 4})
