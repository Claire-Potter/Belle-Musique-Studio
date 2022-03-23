"""
App configuration for Belle Musique Studio home application.
"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    set default_auto_field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
