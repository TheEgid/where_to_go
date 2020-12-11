from django.shortcuts import render


places_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.62, 55.793676]
            },
            "properties": {
                "title": "«Легенды Москвы",
                "placeId": "moscow_legends",
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.64, 55.753676]
            },
            "properties": {
                "title": "Крыши24.рф",
                "placeId": "roofs24",
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
            }
        }
    ]
}


def show_main(request):
    return render(request=request, template_name="index.html",
                  context={"places_geojson": places_geojson})
