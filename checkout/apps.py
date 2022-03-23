"""
App configuration for Belle Musique Studio checkout application.
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Include signals.py
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
