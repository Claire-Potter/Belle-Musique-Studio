"""
Belle Musique Studio checkout app views configuration

After correcting any pylint issues, I was still left with the issue
'class has no objects member', the object is only added when the screen
is  rendered in the browser, so the issue is not valid. I followed
the steps available for the following stack overflow:
https://stackoverflow.com/questions/45135263/class-has-no-objects-member
and created the .pylintrc file to customise the pylint settings to
prevent this error from displaying.

The cache_checkout_data view is utilised
to connect to stripe to process the order payment.

The checkout view renders the checkout template through
the url. It provides the stripe API key settings,
it calls the current shopping bag, to process the contents
as an order.

The checkout_success view returns a successful
checkout's order details. The user will receive
a success message and their order details.

The checkout lesson view renders the checkout template through
the url. The lesson_bag contains the lesson and subscription
to be purchased.

The create_sub view provides the stripe API key settings,
it calls the lesson (stripe product) and subscription (stripe plan)
to process. Payment details are collected and sent through
to stripe to process payment.

The subscribe view renders the subscription template through
the url. The customer and the subscription details are fetched
from the logged in user.

The cancel view is used to cancel a subscription.
This can be completed just after the purchase of the
subscription or from the userprofile, once a subscription
has been added to the SubscriptionLineItem model.

The checkout_lesson_complete view returns a successful
checkout's subscription details. The user will receive
a success message and their subscription details.

Messages definition from:
https://docs.djangoproject.com/en/4.0/ref/contrib/messages/

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
import json
# JavaScript Object Notation (JSON) is a standardized format commonly
# used to transfer data as text that can be sent over a network.
# It’s used by lots of APIs and Databases, and it’s easy for
# both humans and machines to read.
# (https://realpython.com/lessons/what-is-json/#:~:text=import%20json,
#  data%20into%20a%20Python%20list)).
import time
# When support for time zones is enabled, Django stores datetime
# information in UTC in the database, uses time-zone-aware datetime
# objects internally,
# and translates them to the end user’s time zone
# in templates and forms.
# https://docs.djangoproject.com/en/4.0/topics/i18n/timezones/

import stripe
# A Python library for Stripe’s API.
# https://pypi.org/project/stripe/
import djstripe
# dj-stripe implements all of the Stripe models, for Django.
# https://pypi.org/project/dj-stripe/2.2.3/
from django.conf import settings
# The Django settings file contains all of the configuration for a
# web application.
from django.core.mail import send_mail
# send_mail is a function in Django that can send an email using the
# EmailMessage class.
from django.contrib import messages
# Quite commonly in web applications, you need to display a one-time
# notification message (also known as “flash message”) to the user after
# processing a form or
#  some other types of user input.
# For this, Django provides full support for cookie- and session-based
# messaging,
# for both anonymous and authenticated users. The messages framework allows you
# to temporarily store messages in one request and retrieve them for display
# in a subsequent request (usually the next one). Every message is tagged
# with a specific level
# that determines its priority (e.g., info, warning, or error).
from django.http.response import JsonResponse
# An HttpResponse subclass that helps to create a JSON-encoded response.
# It inherits most behavior from its superclass.
# https://docs.djangoproject.com/en/4.0/ref/request-response/
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)
# HttpResponse (source code) provides an inbound HTTP request
# to a Django web
# application with a text response. This class is most frequently used
# as a return object from a Django view.
# get_object_or_404 is a callable within the django.shortcuts module of
# the Django project.
# redirect is a callable within the django.shortcuts module of the Django
# project.
# render is a callable within the django.shortcuts module of the
# Django project.
# reverse is a callable within the django.urls module of the Django project.
from django.views.decorators.http import require_POST
# require_POST is a callable within the django.views.decorators.http
# module of the Django project.
from django.contrib.auth.decorators import login_required
# @login_required: Django's login_required function is used to secure views
# in your web applications by forcing the client to
# authenticate with a valid logged-in User.
from django.template.loader import render_to_string
# render_to_string is a callable within the django.template.loader
# module of the Django project.
from django.views.decorators.csrf import csrf_exempt
# csrf_exempt is a callable within the django.views.decorators.csrf
# module of the Django project.
from djstripe.models import Subscription, Invoice
# Models are imported from djstripe models.py

from home.models import Cover, User, UserSubscription
# Models are imported from home app models.py
from profiles.models import UserProfile
# Model imported from profiles app models.py
from profiles.forms import UserProfileForm
# Form imported from profiles app forms.py
from shopping_bag.contexts import bag_contents, lesson_bag_contents
# Context imported from shopping_bag app contexts.py
from store.models import MusicProduct
# Model imported from store app models.py

from .forms import (OrderForm, SubscribedCustomerForm,
                    SubscriptionLineItemForm)
# Forms are imported from forms.py
from .models import (Order, OrderLineItem, SubscribedCustomer,
                     SubscriptionLineItem)


@require_POST
def cache_checkout_data(request):
    """
    The cache_checkout_data view is utilised
    to connect to stripe to process the order
    payment.

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp

    Created as per the Code Institute 'Boutique Ado'
    project.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e_rr:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e_rr, status=400)


def checkout(request):
    """
    The checkout view renders the checkout template through
    the url. It provides the stripe API key settings,
    it calls the current shopping bag, to process the contents
    as an order. The order_form is utilised to capture the
    user's shipping address details. The user can select to
    save this information to their user profile.
    All order details are saved to the Order and the OrderLineItem
    models.
    Payment details are collected and sent through to stripe to process
    payment.

    request: The requests module allows you to send HTTP
    requests using Python.

    Created as per the Code Institute 'Boutique Ado'
    project.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # if the form has been submitted, the current shopping bag
        # is fetched from the current session
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            # the order is saved and the items in the shopping bag
            # are saved to the OrderLineItem model
            for item_id, item_data in bag.items():
                try:
                    product = MusicProduct.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in (item_data['items_by_size']
                                               .items()):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except MusicProduct.DoesNotExist:
                    messages.error(request, (
                        'One of the products in your bag wasn\'t '
                        'found in our database. '
                        'Please call us for assistance!'))
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        # Process if the shopping bag is empty
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'There\'s nothing in your bag at '
                                    'the moment')
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info the user maintains
        # in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name':  profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='checkout')
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'cover': cover,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    The checkout_success view returns a successful
    checkout's order details. The user will receive
    a success message and their order details.

    request: The requests module allows you to send HTTP
    requests using Python.

    order_number: the unique number generated to identify an order.

    Created as per the Code Institute 'Boutique Ado'
    project.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data,
                                                instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='checkout')
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'cover': cover,
    }

    return render(request, template, context)


@login_required
def checkout_lesson(request):
    """
    The checkout view renders the checkout template through
    the url. The lesson_bag contains the lesson and subscription
    to be purchased. Only one lesson subscription can be
    purchased per checkout because of the integration through
    djstripe set up.

    request: The requests module allows you to send HTTP
    requests using Python.
    """
    # fetch the lesson_bag from the current session if there is no
    # lesson bag, send the error message
    lesson_bag = request.session.get('lesson_bag', {})
    if not lesson_bag:
        messages.error(request, 'There\'s nothing in your bag at '
                                'the moment')
        return redirect(reverse('lessons'))
    # fetch the data required for the checkout_lesson page
    current_bag = lesson_bag_contents(request)
    total = current_bag['lesson_total']
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')
    template = 'checkout/checkout_lesson.html'
    context = {
        'covers': covers,
        'cover': cover,
        'total': total,
    }

    return render(request, template, context)


@login_required
# csrf exempt added, as the csrf details would not validate through
# javascript
@csrf_exempt
def create_sub(request):
    """
    The create_sub view provides the stripe API key settings,
    it calls the lesson (stripe product) and subscription (stripe plan)
    to process. Payment details are collected and sent through
    to stripe to process payment.
    If a customer record already exists on stripe it will be used to create
    the new subscription against. If not a new customer record and a new
    subscription will be created and returned and saved against the
    # User model and the UserSubscription model.
    If a user has default details saved to their userprofile, these details
    will be used to create the customer, however, they are not required.

    request: The requests module allows you to send HTTP
    requests using Python.

    Created as per tutorial and customised for site:
    (https://ordinarycoders.com/blog/article/django-stripe-monthly
     -subscription)
    """
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Reads application/json and returns a response
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = settings.STRIPE_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        (djstripe.models.PaymentMethod
         .sync_from_stripe_data(payment_method_obj))
        # fetch the user customer field if it exists
        user = get_object_or_404(User, username=request.user)
        user_customer = user.customer
        # validate if it exists or not
        if user_customer is None:
            customer_exists = False
        else:
            customer_exists = True
        # if the customer exists retrieve the customer from stripe
        if customer_exists:
            try:
                customer_id = request.user.customer.id
                customer = stripe.Customer.retrieve(f'{customer_id}')

                # At this point, associate the ID of the Customer
                # object with your
                # own internal representation of a customer,
                # if you have one.

                # Subscribe the user to the subscription created
                subscription = stripe.Subscription.create(
                        customer=customer.id,
                        items=[
                            {
                                'price': data['price_id'],
                            },
                        ],
                        expand=['latest_invoice.payment_intent']
                )
                # sync the subscription to the djstripe Subscription model
                djstripe_subscription = (djstripe.models.Subscription.
                                         sync_from_stripe_data(subscription))
                try:
                    # create the subscription against the user in the
                    # UserLineItem model
                    user_line_item = UserSubscription(
                        username=request.user,
                        subscription=djstripe_subscription,
                        subscription_user_id=djstripe_subscription.id,
                        subscription_name=djstripe_subscription.plan
                    )
                    user_line_item.save()
                    request.user.save()
                    username = request.user
                # error message if the user cannot be found
                except username.DoesNotExist:
                    messages.error(request, (
                        'The user wasn\'t found in our database. '
                        'Please call us for assistance!')
                    )
                    subscription.delete()
                return JsonResponse(subscription)
            except Exception as e_rr:
                return JsonResponse({'error': (e_rr.args[0])}, status=403)
        else:
            try:
                # This creates a new Customer and attaches the
                # PaymentMethod in one API call.
                customer = stripe.Customer.create(
                     payment_method=payment_method,
                     email=request.user.email,
                     name=request.user.get_full_name(),
                     phone=profile.default_phone_number,
                     address={
                         # address details provided if they exist,
                         # however not required
                         'city': profile.default_town_or_city,
                         'country': profile.default_country,
                         'line1': profile.default_street_address1,
                         'line2': profile.default_street_address2,
                         'postal_code': profile.default_postcode,
                         'state': profile.default_county
                     },
                     shipping={
                         'name': request.user.get_full_name(),
                         'phone': profile.default_phone_number,
                         'address': {
                             'city': profile.default_town_or_city,
                             'country': profile.default_country,
                             'line1': profile.default_street_address1,
                             'line2': profile.default_street_address2,
                             'postal_code': profile.default_postcode,
                             'state': profile.default_county
                         }, },
                     invoice_settings={
                             'default_payment_method': payment_method}
                         )
                djstripe_customer = (djstripe.models.
                                     Customer.sync_from_stripe_data(customer))
                request.user.customer = djstripe_customer

                # At this point, associate the ID of the Customer
                # object with your
                # own internal representation of a customer,
                # if you have one.

                # Subscribe the user to the subscription created
                subscription = stripe.Subscription.create(
                    customer=customer,
                    items=[
                        {
                            'price': data['price_id'],
                        },
                    ],
                    expand=['latest_invoice.payment_intent']
                )
                # sync the subscription to the djstripe Subscription model
                djstripe_subscription = (djstripe.models
                                         .Subscription.
                                         sync_from_stripe_data(subscription))

                try:
                    # create the subscription against the user in the
                    # UserLineItem model
                    user_line_item = UserSubscription(
                        username=request.user,
                        subscription=djstripe_subscription,
                        subscription_user_id=djstripe_subscription.id,
                        subscription_name=djstripe_subscription.plan
                    )
                    user_line_item.save()
                    request.user.save()
                    username = request.user
                # error message if the user cannot be found
                except username.DoesNotExist:
                    messages.error(request, (
                        'The user wasn\'t found in our database. '
                        'Please call us for assistance!')
                    )
                    subscription.delete()
                return JsonResponse(subscription)
            except Exception as e_rr:
                return JsonResponse({'error': (e_rr.args[0])}, status=403)

    else:
        # Default error response
        return HttpResponse('request method not allowed')


@login_required
def subscribe(request):
    """
    The subscribe view renders the subscription template through
    the url. The customer and the subscription details are fetched
    from the logged in user.
    The subscription_form is utilised to capture the
    user's phone number and the name of the student the subscription
    is for. All customer details are saved to the SubscribedCustomer model
    and the Subscription details are saved to the SubscriptionLineItem
    model.

    request: The requests module allows you to send HTTP
    requests using Python.
    """
    # if the form has been submitted, the current lesson bag
    # is fetched from the current session
    if request.method == 'POST':
        lesson_bag = request.session.get('lesson_bag', {})
        customer_exists = False
        attempt = 1
        while attempt <= 5:
            # determine whether the user has a customer id assigned
            try:
                user_customer_id = request.user.customer.id
                customer_subscribed = (SubscribedCustomer
                                       .objects
                                       .get
                                       (subscribed_customer_id=user_customer_id))
                customer_exists = True
                break
            except SubscribedCustomer.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # if the customer exists, set up the instance of
        # the SubscribedCustomerForm to reference the customer id
        if customer_exists:
            subscription_form = (SubscribedCustomerForm
                                 (request.POST,
                                  instance=(customer_subscribed)))
            subscription_lineitem_form = (SubscriptionLineItemForm(request.
                                                                   POST))
            current_bag = lesson_bag_contents(request)
            total = current_bag['lesson_total']
            # if the forms are valid save the subscription form and proceed
            # to fetch the subscription id from the user
            if (subscription_form.is_valid() and
                subscription_lineitem_form.is_valid()):
                subscription_internal = subscription_form.save(commit=False)
                subscription_lineitem_internal = (subscription_lineitem_form
                                                  .save(commit=False))
                subscription_internal.save()
                user_subscription = (UserSubscription.objects
                                     .filter(username=request.user).latest())
                sub_id = user_subscription.subscription.id
                subscription_check = get_object_or_404(Subscription, id=sub_id)
                # save the subscription to the SubscriptionLineItem model
                try:
                    user_subscription = (UserSubscription.objects
                                         .filter(username=request.user)
                                         .latest())
                    subscribed_id = user_subscription.subscription.id
                    subscription_status = user_subscription.subscription.status
                    subscription_start = (user_subscription.subscription
                                          .current_period_start)
                    subscription_end = (user_subscription.subscription
                                        .current_period_end)
                    subscription_invoice = (user_subscription.subscription
                                            .latest_invoice)
                    (subscription_lineitem_internal
                     .subscribed_id) = subscribed_id
                    (subscription_lineitem_internal
                     .subscription) = user_subscription.subscription
                    (subscription_lineitem_internal
                     .subscription_name) = user_subscription.subscription_name
                    subscription_lineitem_internal.status = subscription_status
                    (subscription_lineitem_internal
                     .customer) = subscription_internal
                    (subscription_lineitem_internal
                     .start_date) = subscription_start
                    (subscription_lineitem_internal
                     .end_date) = subscription_end
                    (subscription_lineitem_internal
                     .latest_invoice) = subscription_invoice
                    subscription_lineitem_internal.price = int(total)
                    subscription_lineitem_internal.quantity = 1
                    (subscription_lineitem_internal
                     .original_lesson_bag) = json.dumps(lesson_bag)
                    subscription_lineitem_internal.save()
                # error if the subscription cannot be found
                except subscription_check.DoesNotExist:
                    messages.error(request, (
                        'The subscription in your bag wasn\'t found in our '
                        'database. '
                        'Please call us for assistance!'))
                    subscription_internal.delete()
                    subscription_lineitem_internal.delete()
                    return redirect(reverse('view_lesson_bag'))
                # collect data and send confirmation email
                user = get_object_or_404(User, username=request.user)
                name = user.first_name
                cust_email = user.email
                event = sub_id
                date = subscription_lineitem_internal.start_date
                plan = user_subscription.subscription_name
                student = subscription_lineitem_internal.student
                subject = render_to_string('checkout/lesson_emails/confirmation_emails/confirmation_email_subject.txt',
                                           {'event': event})
                body = render_to_string('checkout/lesson_emails/confirmation_emails/confirmation_email_body.txt',
                                        {'name': name, 'event': event, 'date': date, 'plan': plan,
                                         'student': student, 
                                         'contact_email': settings.DEFAULT_FROM_EMAIL})
                send_mail(subject,
                          body,
                          settings.DEFAULT_FROM_EMAIL,
                          [cust_email],
                          fail_silently=False)
                return redirect(reverse('checkout_lesson_complete',
                                        args=[sub_id]))
            else:
                # error if the forms could not be validated
                messages.error(request, 'There was an error with your form. \
                    Please double check your information.')
                return HttpResponse(status=400)
        else:
            # process if no customer record exists
            customer = None
            try:
                # the forms data is stipulated
                form_data = {
                    'full_name': request.POST.get('full_name'),
                    'email': request.POST.get('email'),
                    'phone_number': request.POST.get('phone_number'),
                }
                form_data_two = {
                    'student': request.POST.get('student'),
                }
                subscription_form = SubscribedCustomerForm(form_data)
                subscription_lineitem_form = (SubscriptionLineItemForm
                                              (form_data_two))
                user_subscription = (UserSubscription.objects
                                     .filter(username=request.user)
                                     .latest())
                sub_id = user_subscription.subscription.id
                profile = UserProfile.objects.get(user=request.user)
                current_bag = lesson_bag_contents(request)
                total = current_bag['lesson_total']
                subscription = user_subscription.subscription_name
                # the forms are validated and the subscription_form is saved
                if (subscription_form.is_valid() and
                    subscription_lineitem_form.is_valid()):
                    subscription_internal = (subscription_form
                                             .save(commit=False))
                    (subscription_internal
                     .subscribed_customer_id) = user_customer_id
                    subscription_internal.customer = request.user.customer
                    subscription_internal.user_profile = profile
                    subscription_lineitem_internal = (subscription_lineitem_form.save(commit=False))
                    subscription_internal.save()
                    user_subscription = (UserSubscription.objects
                                         .filter(username=request.user)
                                         .latest())
                    sub_id = user_subscription.subscription.id
                    subscription_check = get_object_or_404(Subscription,
                                                           id=sub_id)
                    try:
                        # the latest subscription id is fetched from the user
                        # and the subscription
                        # line item is created and saved
                        user_subscription = (UserSubscription.objects
                                             .filter(username=request.user)
                                             .latest())
                        subscribed_id = user_subscription.subscription.id
                        subscription_status = (user_subscription.subscription
                                               .status)
                        subscription_start = (user_subscription.subscription
                                              .current_period_start)
                        subscription_end = (user_subscription.subscription
                                            .current_period_end)
                        subscription_invoice = (user_subscription.subscription
                                                .latest_invoice)
                        (subscription_lineitem_internal.
                         subscribed_id) = subscribed_id
                        (subscription_lineitem_internal.
                         subscription) = user_subscription.subscription
                        (subscription_lineitem_internal
                         .subscription_name) = (user_subscription.
                                                subscription_name)
                        (subscription_lineitem_internal
                         .status) = subscription_status
                        (subscription_lineitem_internal
                         .customer) = subscription_internal
                        (subscription_lineitem_internal
                         .start_date) = subscription_start
                        (subscription_lineitem_internal
                         .end_date) = subscription_end
                        (subscription_lineitem_internal.
                         latest_invoice) = subscription_invoice
                        subscription_lineitem_internal.price = int(total)
                        subscription_lineitem_internal.quantity = 1
                        (subscription_lineitem_internal.
                         original_lesson_bag) = json.dumps(lesson_bag)
                        subscription_lineitem_internal.save()
                        subscription_check = get_object_or_404(Subscription,
                                                               id=sub_id)
                    # error if the subscription cannot be found
                    except subscription_check.DoesNotExist:
                        messages.error(request, (
                            'The subscription in your bag wasn\'t \
                            found in our database. '
                            'Please call us for assistance!'))
                        subscription_internal.delete()
                        subscription_lineitem_internal.delete()
                        return redirect(reverse('view_lesson_bag'))
                    # customer is saved from the user record
                    customer = user_customer_id
                    # collect data and send confirmation email
                    user = get_object_or_404(User, username=request.user)
                    name = user.first_name
                    cust_email = user.email
                    event = sub_id
                    date = subscription_lineitem_internal.start_date
                    plan = user_subscription.subscription_name
                    student = subscription_lineitem_internal.student
                    subject = render_to_string('checkout/lesson_emails/confirmation_emails/confirmation_email_subject.txt',
                                               {'event': event})
                    body = render_to_string('checkout/lesson_emails/confirmation_emails/confirmation_email_body.txt',
                                            {'name': name, 'event': event, 'date': date, 'plan': plan,
                                             'student': student, 
                                             'contact_email': settings.DEFAULT_FROM_EMAIL})
                    send_mail(subject,
                              body,
                              settings.DEFAULT_FROM_EMAIL,
                              [cust_email],
                              fail_silently=False)
                    return redirect(reverse('checkout_lesson_complete',
                                            args=[sub_id]))

                # error message if the forms fo not validate
                else:
                    messages.error(request, 'There was an error with your \
                        form. \
                        Please double check your information.')
                    return HttpResponse(status=400)
            except Exception as e_rr:
                if customer:
                    customer.delete()
                return HttpResponse(
                    content=f'Request to subscribe \
                    customer received: | ERROR: {e_rr}',
                    status=500)
    else:
        # Process if the lesson bag is empty
        lesson_bag = request.session.get('lesson_bag', {})
        if not lesson_bag:
            messages.error(request, 'There\'s nothing in your bag at'
                           'the moment')
            return redirect(reverse('lessons'))
        # fetch data for page before forms are submitted
        current_bag = lesson_bag_contents(request)
        total = current_bag['lesson_total']
        user_subscription = (UserSubscription.objects
                             .filter(username=request.user).latest())
        sub_id = user_subscription.subscription.id
        profile = UserProfile.objects.get(user=request.user)
        # retrieve phone_number from user profile if it exists
        if profile is None:
            profile_exists = False
            phone_number = None
        else:
            profile_exists = True
            phone_number = profile.default_phone_number
        subscription = user_subscription.subscription_name
        subscription_form = (SubscribedCustomerForm(initial={
                              'full_name': request.user.get_full_name(),
                              'email': request.user.email,
                              'phone_number': phone_number, }))
        subscription_lineitem_form = SubscriptionLineItemForm()
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')

    context = {'covers': covers,
               'cover': cover,
               'total': total,
               'sub_id': sub_id,
               'subscription': subscription,
               'subscription_form': subscription_form,
               'subscription_lineitem_form': subscription_lineitem_form,
               'profile_exists': profile_exists}
    return render(request, 'checkout/subscription.html', context)


def cancel(request):
    """
    The cancel view is used to cancel a subscription.
    This can be completed just after the purchase of the
    subscription or from the userprofile, once a subscription
    has been added to the SubscriptionLineItem model.
    request: The requests module allows you to send HTTP
    requests using Python.

    Created as per tutorial and customised for site:
    (https://ordinarycoders.com/blog/article/django-stripe-monthly-subscription)
    """
    if request.user.is_authenticated:
        # fetch the subscription id from against the user
        user_subscription = (UserSubscription.objects
                             .filter(username=request.user).latest())
        sub_id = user_subscription.subscription.id

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        # access stripe through the api to delete (archive) the
        # subscription
        stripe.Subscription.delete(sub_id)
        # delete it from the user
        user_subscription.delete()
        # delete it from dj_stripe Subscription model
        Subscription.objects.filter(id=sub_id).delete()
        # delete it from SubscriptionLineItem model only if it exits
        subscription_line_item = (SubscriptionLineItem.objects
                                  .filter(subscribed_id=sub_id))
        if subscription_line_item.exists() is True:
            subscription_line_item.delete()
        # if they are still in session with a lesson bag delete the
        # lesson bag
        if 'lesson_bag' in request.session:
            del request.session['lesson_bag']
        user = get_object_or_404(User, username=request.user)
        name = user.first_name
        cust_email = user.email
        event = sub_id
        subject = render_to_string('checkout/lesson_emails/cancellation_emails/cancellation_email_subject.txt',
                                    {'event': event})
        body = render_to_string('checkout/lesson_emails/cancellation_emails/cancellation_email_body.txt',
                                 {'name': name, 'event': event, 
                                  'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(subject,
                  body,
                  settings.DEFAULT_FROM_EMAIL,
                  [cust_email],
                  fail_silently=False)
        messages.success(request,
                         f'Subscription {sub_id} successfully cancelled!')
    except Exception as e_rr:
        return JsonResponse({'error': (e_rr.args[0])}, status=403)

    # direct the user to the user profile, as from a front end
    # perspective, that is where
    # the user will view their active subscriptions from
    return redirect('profile')


def checkout_lesson_complete(request, sub_id):
    """
    The checkout_lesson_complete view returns a successful
    checkout's subscription details. The user will receive
    a success message and their subscription details.

    request: The requests module allows you to send HTTP
    requests using Python.

    sub_id: the unique number used to identify the subscription
    """
    # fetch the required data to be displayed on the page to confirm
    # the subscription
    customer = request.user.customer
    subscribed_customer = get_object_or_404(SubscribedCustomer,
                                            subscribed_customer_id=customer.id)
    subscription_item = get_object_or_404(SubscriptionLineItem,
                                          subscribed_id=sub_id)
    subscription = get_object_or_404(Subscription, id=sub_id)
    # invoice is retrieved and is clickable to open the invoice item
    # on stripe as a new page
    invoice = get_object_or_404(Invoice, id=subscription.latest_invoice.id)
    invoice_link = invoice.hosted_invoice_url
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')
    messages.success(request, f'Subscription successfully processed! \
        Your subscription number is {sub_id}. A confirmation \
        email will be sent to {subscribed_customer.email}.')
    # if the lesson bag is still in the session delete the lesson bag
    if 'lesson_bag' in request.session:
        del request.session['lesson_bag']

    template = 'checkout/checkout_lesson_complete.html'
    context = {
        'subscribed_customer': subscribed_customer,
        'subscription_item': subscription_item,
        'sub_id': sub_id,
        'invoice_link': invoice_link,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context)
