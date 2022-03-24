"""
App configuration for Belle Musique Studio store application.
"""
from django.apps import AppConfig


class StoreConfig(AppConfig):
    """
    definition of default auto field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
