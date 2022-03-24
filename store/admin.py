"""
Belle Musique Studio store app admin configuration

Definitions from https://www.fullstackpython.com
unless stated otherwise
"""
from django.contrib import admin
# The Django admin is an automatically-generated user interface
# for Django models. The admin interface can be heavily customized

from .models import Category, MusicProduct
# Models are imported from models.py


class ProductAdmin(admin.ModelAdmin):
    """
     The Product admin provides a view of the music product
     model and allows staff to edit or delete.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'has_sizes',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
     The Category admin provides a view of the category
     model and allows staff to edit or delete.
    """
    list_display = (
        'call_name',
        'name',
    )


admin.site.register(MusicProduct, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
