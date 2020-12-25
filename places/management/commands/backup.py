import os
import json
import codecs
from django.conf import settings
from django.core.management.base import BaseCommand


def correct_db_backup_file(db_backup_file):
    with codecs.open(db_backup_file, 'r') as f:
        backups = json.load(f)
    with open(db_backup_file, 'w', encoding='utf-8') as f:
        json.dump(backups, indent=4, fp=f)


class Command(BaseCommand):
    help = 'Make backup db file'

    def handle(self, *args, **options):
        db_backup_file = 'db.json'
        db_backup_filepath = settings.BASE_DIR
        os.system(f'python manage.py dumpdata --indent=4 > {db_backup_file}')
        correct_db_backup_file(db_backup_file)
        print(f'{db_backup_filepath=}; {db_backup_file=}')
