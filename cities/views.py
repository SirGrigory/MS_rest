from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django_filters.rest_framework import DjangoFilterBackend
from .service import ShopFilter


class CitiesList(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetsList(APIView):

    def get(self, request, pk):
        streets = Street.objects.all().filter(city_id=pk)
        serializer = StreetSerializer(instance=streets, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class ShopListCreate(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter
    