from rest_framework import serializers
from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['name']


class StreetSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Street
        fields = ['name', 'city']


class ShopSerializer(serializers.ModelSerializer):
    street = serializers.StringRelatedField(many=False)
    city = serializers.ReadOnlyField(source='street.city.name')

    class Meta:
        model = Shop
        fields = ['name', 'city', 'street',
                  'house_num', 'opening_time', 'closing_time']
