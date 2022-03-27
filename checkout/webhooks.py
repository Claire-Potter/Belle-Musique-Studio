"""
Belle Musique Studio dj stripe webhooks configuration

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
from djstripe import webhooks
# dj-stripe implements all of the Stripe models, for Django.
# https://pypi.org/project/dj-stripe/2.2.3/



@webhooks.handler("customer.subscription.created")



@webhooks.handler("customer.subscription.deleted")
def customer_subscription_deleted_event_listener(event, **kwargs):
    """
    Email to be created and sent when a customer's
    subscription is cancelled.
    """
    intent = event.data.object
    user_name = intent.metadata.username
    user = get_object_or_404(User, username=user_name)
    name = user.first_name
    cust_email = user.email
    subject = render_to_string('lesson_emails/cancellation_emails/'
                               'cancellation_email_subject.txt',
                               {'event': event}),
    body = render_to_string(
            'lesson_emails/cancellation_emails/cancellation_email_body.txt',
            {'name': name, 'event': event,
             'contact_email': settings.DEFAULT_FROM_EMAIL})
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email],
        fail_silently=False,
    )