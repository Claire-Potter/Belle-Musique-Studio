"""
App configuration for Belle Musique Studio profile application.
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    set default_auto_field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
