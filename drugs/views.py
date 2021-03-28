from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from drugs.models import Drug, StoreDrugs
from drugs.serializers import DrugSerializer, StoreDrugsSerializer


class DrugViewSet(viewsets.GenericViewSet, viewsets.generics.ListAPIView, viewsets.generics.RetrieveAPIView):
    serializer_class = DrugSerializer
    queryset = Drug.objects.raw('select * from drugs')

    filter_backends = [
        SearchFilter
    ]
    search_fields = ['name']

    def get_object(self):
        return Drug.objects.raw('select * from drugs where id=%s', [self.kwargs.get('pk')])[0]

    @action(methods=['get'], detail=True)
    def stores(self, request, *args, **kwargs):
        queryset = StoreDrugs.objects.raw('select * from drugs_storedrugs where drug_id=%s', [kwargs.get('pk')])
        queryset = [x for x in queryset]
        serializer = StoreDrugsSerializer(queryset, many=True)
        return Response(serializer.data, 200)
