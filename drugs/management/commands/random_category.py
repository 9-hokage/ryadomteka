from django.core.management.base import BaseCommand
import random

from drugs.models import Drug


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        drugs = Drug.objects.all()
        for drug in drugs:
            category = random.randint(1, 237)
            drug.category_id = category
            drug.save()
        self.stdout.write(self.style.SUCCESS('Successfully'))
