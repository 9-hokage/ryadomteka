from rest_framework import filters


class CovidStatisticByCountry(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if 'country' in request.query_params:
            return queryset.filter(country__name=request.query_params['country'])
        return queryset