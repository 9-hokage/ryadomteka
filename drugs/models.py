from common.models import User, Country
from django.db import models

# Create your models here.
from stores.models import Store


class DrugCategory(models.Model):
    name = models.CharField(max_length=1000)


class Drug(models.Model):
    name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    form_drug = models.CharField(max_length=255)
    recipe = models.BooleanField()
    reg_id = models.CharField(max_length=255)
    atc_classification = models.CharField(max_length=255)
    producer = models.CharField(max_length=255, null=True)
    classification = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    country = models.ForeignKey(Country, models.SET_NULL, null=True)
    image = models.CharField(null=True, blank=True, max_length=255)
    category = models.ForeignKey(DrugCategory, models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)

    @property
    def min_price(self):
        return self.storedrugs_set.order_by('price').first().price

    @property
    def min_quantity(self):
        return self.storedrugs_set.order_by('quantity').first().quantity


    class Meta:
        db_table = 'drugs'


class StoreDrugs(models.Model):
    drug = models.ForeignKey(Drug, models.CASCADE)
    store = models.ForeignKey(Store, models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)


class BoughtDrugs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    buy_date = models.DateTimeField(null=True)

    quantity = models.IntegerField(default=1)
