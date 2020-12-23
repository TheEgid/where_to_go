import os
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Make backup db file'

    def handle(self, *args, **options):
        db_backup_file = 'db.json'
        db_backup_filepath = settings.BASE_DIR
        os.system(f'python manage.py dumpdata --indent=4 > {db_backup_file}')
        print(f'{db_backup_filepath=}; {db_backup_file=}')
