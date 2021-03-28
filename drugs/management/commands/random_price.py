from django.core.management.base import BaseCommand
import random

from drugs.models import Drug, StoreDrugs


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        drugs = StoreDrugs.objects.all()
        for drug in drugs:
            price = random.randint(100, 10000)
            drug.price = price
            drug.save()
        self.stdout.write(self.style.SUCCESS('Successfully'))
