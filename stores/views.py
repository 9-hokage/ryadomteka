from rest_framework import viewsets
# Create your views here.
from rest_framework.filters import SearchFilter

from .filters import StoreByCityFilter, CustomSearchFilter
from .models import Store
from .serializers import StoreSerializer


class StoreViewSet(viewsets.GenericViewSet, viewsets.generics.ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    filter_backends = [
        StoreByCityFilter,
        CustomSearchFilter
    ]
    search_fields = ['name']

