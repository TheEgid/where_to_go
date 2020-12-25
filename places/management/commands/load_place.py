from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point
from places.models import Place, Image
from places.utils import clear_string
import pprint
import requests


class LoadPlaceError(CommandError):
    pass


def create_place(new_place):
    try:
        lon = float(new_place['coordinates']['lng'])
        lat = float(new_place['coordinates']['lat'])
        pnt = Point(lon, lat)
        new_place = Place.objects.get_or_create(
            coordinates=pnt,
            short_description=clear_string(new_place['description_short']),
            long_description=clear_string(new_place['description_long']),
            # imgs
            title=clear_string(new_place['title']),
        )
        return new_place
    except TypeError:
        raise LoadPlaceError("Error! Please check json filepath")



def get_place_from_web(filepath):
    loaded_json = ""
    response = requests.get(filepath, verify=False)
    if response.ok:
        loaded_json = response.json()
    return loaded_json


# http://адрес/файла.json
class Command(BaseCommand):
    help = 'Add json content'

    def add_arguments(self, parser):
        parser.add_argument('filepath', nargs='+', type=str)

    def handle(self, *args, **options):
        filepath = options['filepath'][0]

        new_place = get_place_from_web(filepath)
        added_place = create_place(new_place)
        if added_place[1]:
            pprint.pprint(f"Place {added_place[0]} added successful!")
        else:
            pprint.pprint(f"Place {added_place[0]} already exists!")


        # print(*args)

    # def handle(self, *args, **options):
    #     for poll_id in options['poll_ids']:
    #         try:
    #             poll = Poll.objects.get(pk=poll_id)
    #         except Poll.DoesNotExist:
    #             raise CommandError('Poll "%s" does not exist' % poll_id)
    #
    #         poll.opened = False
    #         poll.save()
    #
    #         self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))


#python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9F%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D0%BA%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B2%D0%B8%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9%20%D0%BD%D0%B0%2060-%D0%BC%20%D1%8D%D1%82%D0%B0%D0%B6%D0%B5%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0-%D0%A1%D0%B8%D1%82%D0%B8.json

