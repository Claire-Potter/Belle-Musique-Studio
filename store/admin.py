from django.contrib import admin

from .models import Category, MusicProduct


class ProductAdmin(admin.ModelAdmin):
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
    list_display = (
        'call_name',
        'name',
    )


admin.site.register(MusicProduct, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
