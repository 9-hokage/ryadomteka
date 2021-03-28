from rest_framework import filters
from rest_framework.filters import SearchFilter

from stores.models import Store


class StoreByCityFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if 'city' in request.query_params:
            return Store.objects.raw('SELECT "STORES"."ID", "STORES"."NAME", "STORES"."ADDRESS", "STORES"."LONGITUDE", "STORES"."LATITUDE", "STORES"."PHONE", "STORES"."WORK_TIME_WEEKDAYS", "STORES"."WORK_TIME_SAT", "STORES"."WORK_TIME_SUN", "STORES"."STATUS", "STORES"."CITY_ID" FROM "STORES" INNER JOIN "RYADOMTEKA_CITIES" ON ("STORES"."CITY_ID" = "RYADOMTEKA_CITIES"."ID") WHERE "RYADOMTEKA_CITIES"."NAME" = %s',[request.query_params.get('city')])
        return queryset

class CustomSearchFilter(SearchFilter):
    def filter_queryset(self, request, queryset, view):
        if 'search' in request.query_params:
            return Store.objects.raw(
            'SELECT "STORES"."ID", "STORES"."NAME", "STORES"."ADDRESS", "STORES"."LONGITUDE", "STORES"."LATITUDE", "STORES"."PHONE", "STORES"."WORK_TIME_WEEKDAYS", "STORES"."WORK_TIME_SAT", "STORES"."WORK_TIME_SUN", "STORES"."STATUS", "STORES"."CITY_ID" FROM "STORES" WHERE UPPER("STORES"."NAME") LIKE UPPER(TRANSLATE(%s USING NCHAR_CS)) ESCAPE TRANSLATE(\'\\\' USING NCHAR_CS)',
            [request.query_params.get('search')])
        return queryset
