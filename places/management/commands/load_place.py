import codecs
from pathlib import Path
import requests
from PIL import Image
from io import BytesIO
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point
from places.models import Place, Image


class LoadPlaceError(CommandError):
    pass


def create_place(new_place_json):
    try:
        lon = float(new_place_json['coordinates']['lng'])
        lat = float(new_place_json['coordinates']['lat'])
        pnt = Point(lon, lat)
        new_place = Place.objects.get_or_create(
            title=clean_string(new_place_json['title']),
            defaults={'coordinates': pnt,
                      'short_description':
                          clean_string(new_place_json['description_short']),
                      'long_description':
                          clean_string(new_place_json['description_long'])
                      }
        )
        return new_place
    except TypeError:
        raise LoadPlaceError("Error! Please check json filepath")


def clean_string(line):
    line = line.replace("", "")
    return codecs.decode(codecs.encode(
        line, 'latin-1', 'backslashreplace'), 'unicode-escape')


def save_picture(url, new_name):
    filename = settings.MEDIA_ROOT / new_name
    response = requests.get(url)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    img.save(filename)


def create_images(new_place_obj, new_place_json):
    image_links = new_place_json['imgs']
    for count, img_link in enumerate(image_links):
        new_name = f"{new_place_obj.title.replace(' ', '_')}_" \
                   f"{Path(img_link).name}"
        image_obj, status = Image.objects.get_or_create(
            image=new_name,
            defaults={
                'location': new_place_obj,
                'number': count
            }
        )
        if status:
            save_picture(img_link, new_name)
            print(f"Image {image_obj} added successful!")
        else:
            print(f"Image {image_obj} already exists!")


def get_place_json_from_web(filepath):
    loaded_json = ""
    response = requests.get(filepath)
    if response.ok:
        loaded_json = response.json()
    return loaded_json


class Command(BaseCommand):
    help = 'Add json content'

    def add_arguments(self, parser):
        parser.add_argument('filepath', nargs='+', type=str)

    def handle(self, *args, **options):
        new_place_filepath = options['filepath'][0]
        new_place_json = get_place_json_from_web(new_place_filepath)
        new_place_obj, status = create_place(new_place_json)
        if status:
            print(f"Place {new_place_obj} added successful!")
            create_images(new_place_obj, new_place_json)
        else:
            print(f"Place {new_place_obj} already exists!")
