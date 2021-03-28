from rest_framework import filters


class DrugByCityFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if 'city' in request.query_params:
            return queryset.filter(city=request.query_params.get('city'))
        return queryset