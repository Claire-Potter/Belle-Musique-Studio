"""
App configuration for Belle Musique Studio lessons application.
"""
from django.apps import AppConfig


class LessonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lessons'
