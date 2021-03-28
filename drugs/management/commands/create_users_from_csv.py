import csv
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    """manage.py import_users --csv='/Users/user/usuariosweb.csv' --encoding='iso-8859-1'"""
    help = 'Imports users based on a CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--csv',
            action='store',
            dest='file',
            help='File path of CSV containing users list'
        )

        parser.add_argument(
            '--encoding',
            action='store',
            dest='encoding',
            help='encoding of file'
        )

    def handle(self, *args, **options):
        User = get_user_model()

        if options['file']:
            with open(options['file'], encoding=options.get('encoding', 'utf-8')) as csvfile:
                reader = csv.DictReader(csvfile)
                created_users = existing_users = errors = 0
                users_with_errors = []
                for row in reader:
                    if row['USERNAME'] and row['EMAIL']:
                        try:
                            User.objects.create_user(
                                username=row['USERNAME'], email=row['EMAIL'],password=row['PASSWORD'],first_name=row['NAME'],last_name=row['SURNAME'],city_id=row['CITY_ID'])
                            print('{0} - {1}'.format(row['USERNAME'], 'Created' ))
                        except Exception as e:
                            errors += 1
                            users_with_errors.append(row['USERNAME'])
                            self.stdout.write(self.style.ERROR(e))
                self.stdout.write(self.style.SUCCESS(
                    'Successfully imported {0} users, '
                    '{1} already exist, {2} users with errors'.format(
                        created_users,
                        existing_users,
                        errors
                    ))
                )
                if users_with_errors:
                    print('Users with errors: {0}'.format(','.join(users_with_errors)))
        else:
            self.stdout.write(self.style.ERROR('No file provided'))