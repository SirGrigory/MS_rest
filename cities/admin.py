from django.contrib import admin
from .models import City, Street, Shop

# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'city']
    ordering = ['id']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'street', 'house_num',
                    'opening_time', 'closing_time']
