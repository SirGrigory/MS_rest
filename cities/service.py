from django_filters import rest_framework as filters
from .models import Shop
from django.utils import timezone


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class ShopFilter(filters.FilterSet):
    street = CharFilterInFilter(field_name='street__id', lookup_expr='in', label='street ID')
    city = CharFilterInFilter(field_name='street__city__id', lookup_expr='in', label='city ID')
    opened = filters.BooleanFilter(method='open_close_filter', label='open')

    def open_close_filter(self, queryset, name, value):
        time = timezone.now() - timezone.timedelta(hours=0)
        print(time)
        if value:
            return queryset.filter(opening_time__lt=time, closing_time__gt=time)
        else:
            return queryset.exclude(opening_time__lt=time, closing_time__gt=time)

    class Meta:
        model = Shop
        fields = ['street', 'city', 'opened']
