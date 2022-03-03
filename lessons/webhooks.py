from djstripe import webhooks
from djstripe.models import Customer, Subscription

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def __init__(self, request):
    self.request = request


@webhooks.handler("customer.subscription.created")
def customer_created_event_listener(event, **kwargs):
    """.git/"""
    cust_email = customer.email
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
