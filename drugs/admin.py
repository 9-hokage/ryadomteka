from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Drug, DrugCategory, BoughtDrugs


# Register your models here.

class DrugResource(resources.ModelResource):
    class Meta:
        model = Drug


@admin.register(Drug)
class DrugAdmin(ImportExportModelAdmin):
    resource_class = DrugResource
    list_display = ('name', 'price',)


@admin.register(DrugCategory)
class DrugCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(BoughtDrugs)