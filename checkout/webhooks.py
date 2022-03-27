"""
Belle Musique Studio dj stripe webhooks configuration

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
from django.conf import settings
# The Django settings file contains all of the configuration for a
# web application.
from django.core.mail import send_mail
# send_mail is a function in Django that can send an email using the
# EmailMessage class.
from django.shortcuts import get_object_or_404
# get_object_or_404 is a callable within the django.shortcuts module of the
# Django project.
from django.template.loader import render_to_string
# render_to_string is a callable within the django.template.loader
# module of the Django project.
from djstripe import webhooks
# dj-stripe implements all of the Stripe models, for Django.
# https://pypi.org/project/dj-stripe/2.2.3/

from home.models import User
# Model imported from home app models.py


def __init__(self, request):
        self.request = request


@webhooks.handler('customer.subscription.created')
def customer_created_event_listener(event, **kwargs):
    """.git/"""

    send_mail(
           'testing',
           'sending email',
           'bellemusiquestudio@gmail.com',
           ['clairepotter019@gmail.com'],
           fail_silently=False,)



@webhooks.handler("customer.subscription.deleted")
def customer_subscription_deleted_event_listener(event, **kwargs):
    """
    Email to be created and sent when a customer's
    subscription is cancelled.
    """
    
    send_mail(
           'testing',
           'sending email',
           'bellemusiquestudio@gmail.com',
           ['clairepotter019@gmail.com'],
           fail_silently=False)
