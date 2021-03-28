from django.core.management.base import BaseCommand
import random

from drugs.models import Drug


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        drugs = Drug.objects.all()
        for drug in drugs:
            rand_quality = random.randint(0, 7)
            drug.quantity = rand_quality
            drug.save()
        self.stdout.write(self.style.SUCCESS('Successfully'))
