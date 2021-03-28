from django.core.management.base import BaseCommand
import random

from drugs.models import Drug


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        drugs = Drug.objects.all()
        for drug in drugs:
            country = random.randint(851, 1042)
            print(country)
            drug.country_id = country
            drug.save()
        self.stdout.write(self.style.SUCCESS('Successfully'))
