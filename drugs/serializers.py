from rest_framework import serializers

from drugs.models import Drug, StoreDrugs
from stores.serializers import StoreSerializer


class DrugSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    min_price = serializers.IntegerField()
    min_quantity = serializers.IntegerField()

    class Meta:
        model = Drug
        fields = '__all__'


class StoreDrugsSerializer(serializers.ModelSerializer):
    store = StoreSerializer()

    class Meta:
        model = StoreDrugs
        fields = '__all__'
