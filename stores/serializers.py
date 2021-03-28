from rest_framework import serializers

from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name')
    class Meta:
        model = Store
        fields = '__all__'
