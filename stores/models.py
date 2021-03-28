from django.db import models

# Create your models here.
from common.models import City


class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    work_time_weekdays = models.CharField(max_length=255)
    work_time_sat = models.CharField(max_length=255)
    work_time_sun = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='open')
    city= models.ForeignKey(City, models.CASCADE, null=True)

    class Meta:
        db_table = 'stores'





