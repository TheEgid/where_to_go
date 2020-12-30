import pprint
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings


class Command(BaseCommand):

    help = 'Create Superuser account'

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = settings.SUPERUSER_LOGIN
            email = settings.SUPERUSER_EMAIL
            password = settings.SUPERUSER_PASSWORD
            pprint.pprint(f'Creating account for {username}, {email}')
            admin = User.objects.create_superuser(email=email,
                                                  username=username,
                                                  password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')