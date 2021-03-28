from django.core.management.base import BaseCommand
import random

from drugs.models import Drug, StoreDrugs


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        drugs = Drug.objects.all()
        for drug in drugs:
            store = random.randint(11545, 14430)
            price = random.randint(100, 14430)
            StoreDrugs.objects.create(store_id=store, quantity=random.randint(1, 7), drug=drug, price=price)
        self.stdout.write(self.style.SUCCESS('Successfully'))
