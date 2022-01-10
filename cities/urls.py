from django.urls import path
from .views import CitiesList, StreetsList, ShopListCreate

urlpatterns = [
    path('city/', CitiesList.as_view(), name='cities-list'),
    path('city/<int:pk>/street/', StreetsList.as_view(), name='streets-list'),
    path('shop/', ShopListCreate.as_view(), name='shop-create'),
]
