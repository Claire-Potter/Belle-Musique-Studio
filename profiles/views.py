"""
Belle Musique Studio profile app views configuration:

The profile view is set up to display the user's profile.
The profile contains the user's default address
details, subscription summary and order summary.

The order history view is set up to display the user's
completed orders.

The subscription detail view is set up to display the user's
current subscriptions.
The user is able to cancel any active subscription from this view.

Created as per the Code Institute 'Boutique Ado' project.

Messages definition from:
https://docs.djangoproject.com/en/4.0/ref/contrib/messages/

Definitions from https://www.fullstackpython.com
unless stated otherwise.

"""
from django.contrib import messages
# Quite commonly in web applications, you need to display a one-time
# notification
# message (also known as “flash message”) to the user after processing
# a form or
#  some other types of user input.

# For this, Django provides full support for cookie- and
# session-based messaging,
# for both anonymous and authenticated users. The messages
# framework allows you
# to temporarily store messages in one request and retrieve them for
# display in a
# subsequent request (usually the next one). Every message is tagged with
# a specific level
# that determines its priority (e.g., info, warning, or error).
from django.shortcuts import get_object_or_404, render
# get_object_or_404 is a callable within the django.shortcuts module of
# the Django project.
# render is a callable within the django.shortcuts module
# of the Django project.
from djstripe.models import Invoice, Subscription
# Models are imported from djstripe models.py

from checkout.models import Order, SubscribedCustomer, SubscriptionLineItem
# Models are imported from checkout app models.py
from home.models import Cover
# Model is imported from home app models.py

from .forms import UserProfileForm
# Forms are imported from forms.py
from .models import UserProfile
# Model is imported from models.py


def profile(request):
    """
    The profile view is set up to display the user's profile.
    The profile contains the user's default address
    details, subscription summary and order summary.
    """
    # fetch the logged in user's profile
    profile = get_object_or_404(UserProfile, user=request.user)
    # if the form has been submitted and posted validate and save
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    # fetch the data for the initial page
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    subscribed_customers = profile.subscribed_customers
    subscription_items = subscribed_customers.subscription_customer.all()
    template = 'profiles/profile.html'
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='account_profile')
    context = {'covers': covers,
               'cover': cover,
               'form': form,
               'orders': orders,
               'subscribed_customers': subscribed_customers,
               'subscription_items': subscription_items,
               'on_profile_page': True}

    return render(request, template, context)


def order_history(request, order_number):
    """
    The order history view is set up to display the user's
    completed orders.

    request: The requests module allows you to send HTTP
    requests using Python.

    order_number: the unique number generated to identify an order.

    Created as per the Code Institute 'Boutique Ado'
    project.
    """
    order = get_object_or_404(Order, order_number=order_number)
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='checkout')

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context)


def subscription_detail(request, subscribed_id):
    """
    The subscription detail view is set up to display the user's
    current subscriptions.
    The user is able to cancel any active subscription from this view.

    request: The requests module allows you to send HTTP
    requests using Python.

    subscribed_id: the unique number generated to identify a subscription.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    subscribed_customer = get_object_or_404(SubscribedCustomer,
                                            user_profile=profile)
    subscription_item = get_object_or_404(SubscriptionLineItem,
                                          subscribed_id=subscribed_id)
    subscription = get_object_or_404(Subscription, id=subscribed_id)
    # the user is able to access the invoice on stripe through the url
    invoice = get_object_or_404(Invoice, id=subscription.latest_invoice.id)
    invoice_link = invoice.hosted_invoice_url
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')

    messages.info(request, (
        f'This is a past confirmation for subscription '
        f'{subscription_item.subscribed_id}. '
        f'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_lesson_complete.html'
    context = {
        'subscribed_customer': subscribed_customer,
        'from_profile': True,
        'covers': covers,
        'cover': cover,
        'subscription_item': subscription_item,
        'invoice_link': invoice_link,
    }

    return render(request, template, context)
