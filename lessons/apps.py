"""
App configuration for Belle Musique Studio lessons application.
"""
from django.apps import AppConfig


class LessonsConfig(AppConfig):
    """
    set default_auto_field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lessons'
