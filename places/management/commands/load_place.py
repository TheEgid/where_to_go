from django.core.management.base import BaseCommand, CommandError
import requests


# from places.models import Question as Poll


#python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%98%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%20%D0%9F%D1%80%D0%B5%D0%BF%D0%BE%D0%B4%D0%BE%D0%B1%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%A1%D0%B5%D1%80%D0%B3%D0%B8%D1%8F%20%D0%A0%D0%B0%D0%B4%D0%BE%D0%BD%D0%B5%D0%B6%D1%81%D0%BA%D0%BE%D0%B3%D0%BE.json


def get_place_json_from_web(filepath):
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
        import pprint
        new_place = get_place_json_from_web(filepath)
        pprint.pprint(new_place)

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


