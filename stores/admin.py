from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from stores.models import Store


class StoreResource(resources.ModelResource):
    class Meta:
        model = Store


@admin.register(Store)
class DrugAdmin(ImportExportModelAdmin):
    resource_class = StoreResource
    list_display = ('name',)
