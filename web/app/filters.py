import django_filters
from django import forms
from .models import Product, Category

class ProductFilter(django_filters.FilterSet):
    # Строковое поле с подстрочным поиском
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name (contains)')

    # Числовое поле с фильтрацией по минимальному и максимальному значению
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')

    # Поле типа float с фильтрацией по диапазону
    rating = django_filters.RangeFilter(label='Rating (range)')

    # Булевое поле
    is_available = django_filters.BooleanFilter(label='Available')

    # Фильтрация по подстроке в описании
    description = django_filters.CharFilter(lookup_expr='icontains', label='Description (contains)')

    # Множественный выбор категорий (ManyToManyField)
    categories = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '10'}),  # Исправленный виджет
        label='Categories'
    )

    # Фильтрация по диапазону дат
    created_at = django_filters.DateFromToRangeFilter(label='Created (range)')

    # Фильтрация по диапазону дат и времени
    updated_at = django_filters.DateTimeFromToRangeFilter(label='Updated (range)')

    # Фильтрация по фиксированным значениям
    color = django_filters.ChoiceFilter(
        choices=Product._meta.get_field('color').choices,
        label='Color'
    )

    # Фильтрация по времени (в рамках модели, не очень уместно, но для примера)
    created_time = django_filters.TimeFilter(field_name='created_at', lookup_expr='time', label='Created Time')

    # Сортировка результатов
    ordering = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('price', 'price'),
            ('created_at', 'created_at'),
        ),
        field_labels={
            'name': 'Name',
            'price': 'Price',
            'created_at': 'Date Created',
        },
        label='Order By'
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'min_price',
            'max_price',
            'rating',
            'is_available',
            'description',
            'categories',
            'created_at',
            'updated_at',
            'color',
            'created_time',
            'ordering'
        ]
