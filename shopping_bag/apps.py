"""
App configuration for Belle Musique Studio shopping_bag application.
"""
from django.apps import AppConfig


class ShoppingBagConfig(AppConfig):
    """
    set the default auto field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping_bag'
