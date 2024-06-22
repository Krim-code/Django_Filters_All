from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'is_available', 'created_at', 'updated_at')
    list_filter = ('is_available', 'color', 'created_at', 'updated_at', 'categories')
    search_fields = ('name', 'description')
    ordering = ('name', 'price')
    filter_horizontal = ('categories',)

    # Для редактирования ManyToMany через встроенный виджет
    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'rating', 'is_available', 'description', 'categories', 'color')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
