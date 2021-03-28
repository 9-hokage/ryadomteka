from django.core.management.base import BaseCommand
import random

from common.models import User
from drugs.models import Drug, StoreDrugs, BoughtDrugs


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        dates = [
            '2020-03-25',
            '2020-04-02',
            '2020-04-12',
            '2020-04-26',
            '2020-05-05',
            '2020-05-12',
            '2020-05-17',
            '2020-05-31',
            '2020-06-12',
            '2020-06-15',
            '2020-06-27',
            '2020-07-06',
            '2020-08-17',
            '2020-09-06',
            '2020-09-12',
            '2020-09-14',
            '2020-10-21',
            '2020-10-31',
            '2020-11-11',
            '2020-11-14',
            '2020-11-22',
            '2020-11-26',
            '2020-12-07',
            '2020-12-16',
            '2020-12-26',
        ]

        for i in range(1000):
            drug = Drug.objects.order_by('?')[0]
            user = User.objects.order_by('?')[0]
            quantity = random.randint(1, 4)
            buy_date = random.choice(dates)
            BoughtDrugs.objects.create(drug=drug, quantity=quantity, buy_date=buy_date,user=user)
        self.stdout.write(self.style.SUCCESS('Successfully'))
