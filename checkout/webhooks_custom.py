"""
Belle Musique Studio custom webhooks configuration

Completed as per Code Institute 'Boutique Ado' Project

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
import stripe
# A Python library for Stripe’s API.
# https://pypi.org/project/stripe/
from django.conf import settings
# The Django settings file contains all of the configuration for a
# web application.
from django.http import HttpResponse
# HttpResponse (source code) provides an inbound HTTP request to a Django web
# application with a text response. This class is most frequently used
# as a return object from a Django view.
from django.views.decorators.csrf import csrf_exempt
# csrf_exempt is a callable within the django.views.decorators.csrf
# module of the Django project.
from django.views.decorators.http import require_POST
# require_POST is a callable within the django.views.decorators.http
# module of the Django project.
from checkout.webhook_handler import StripeWhHandler
# webhook handler imported from checkout app webhook_handler.py
from .webhooks import customer_created_event_listener, customer_subscription_deleted_event_listener


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e_rr:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e_rr:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e_rr:
        return HttpResponse(content=e_rr, status=400)

    # Set up a webhook handler
    handler = StripeWhHandler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': (handler.handle_payment_intent_payment_failed),
        'payment_intent.payment_failed': (handler.handle_payment_intent_payment_failed), 
        'customer.subscription.created': (handler.handle_customer_subscription_created),
        'customer.subscription.deleted': (handler.handle_customer_subscription_deleted)}

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response


def __init__(self, request):
    self.request = request
