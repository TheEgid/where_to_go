import pprint
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from environs import Env

env = Env()
env.read_env()


class Command(BaseCommand):

    help = 'Create Superuser account'

    def add_arguments(self, parser):
        parser.add_argument('-email', nargs='+', type=str,
                            default=env.str("SUPERUSER_EMAIL"),
                            help='superuser email for django admin')
        parser.add_argument('-login', nargs='+', type=str,
                            default=env.str("SUPERUSER_LOGIN"),
                            help='superuser email for django admin')
        parser.add_argument('-password', nargs='+', type=str,
                            default=env.str("SUPERUSER_PASSWORD"),
                            help='superuser email for django admin')

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            email = options['email']
            username = options['username']
            password = options['password']
            pprint.pprint(f'Creating account for {username}, {email}')
            admin = User.objects.create_superuser(email=email,
                                                  username=username,
                                                  password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')