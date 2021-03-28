from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from common.models import City, Country, CovidStatistic, News

admin.site.register([City, CovidStatistic, News])

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country

@admin.register(Country)
class DrugAdmin(ImportExportModelAdmin):
    resource_class = CountryResource
    list_display = ('name','latitude','longitude',)