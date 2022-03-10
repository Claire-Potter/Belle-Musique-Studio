""".git/"""
import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from djstripe import webhooks
from djstripe.models import Customer

from checkout.webhook_handler import StripeWhHandler
from home.models import User
from .models import SubscribedCustomer


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
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

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


@webhooks.handler("customer.subscription.created")
def customer_created_event_listener(event, **kwargs):
    """.git/"""
    intent = event.data.object
    user_name = intent.metadata.username
    user = get_object_or_404(User, username=user_name)
    user_customer = user.customer
    sub_id = user.subscription.id
    subscribed_customer = get_object_or_404(SubscribedCustomer, customer=user_customer)
    cust_email = subscribed_customer.email
    subject = render_to_string(
            'lesson_emails/confirmation_emails/confirmation_email_subject.txt',
            {'event': event})
    body = render_to_string(
            'lesson_emails/confirmation_emails/confirmation_email_body.txt',
            {'event': event, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    send_mail(
           subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email],
            fail_silently=False,
)
