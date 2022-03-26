"""
Belle Musique Studio signals configuration

Completed as per Code Institute 'Boutique Ado' Project

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
from django.db.models.signals import post_delete, post_save
# post_delete is a callable within the django.db.models.signals
# module of the Django project.
# post_save is a callable within the django.db.models.signals
# module of the Django project.
from django.dispatch import receiver
# The Signal class allows certain senders to notify a set of receivers
#  that some action has taken place across Django apps within the
# same project.
from .models import OrderLineItem
# Model imported from checkout models.py


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
