""".git/"""
import json
import time

import stripe
import djstripe
from django.conf import settings
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from djstripe.models import Subscription

from home.models import Cover, User, UserLineItem
from profiles.models import UserProfile
from shopping_bag.contexts import bag_contents, lesson_bag_contents
from store.models import MusicProduct

from .forms import OrderForm, SubscribedCustomerForm
from .models import Order, OrderLineItem, SubscribedCustomer, SubscriptionLineItem


@require_POST
def cache_checkout_data(request):
    """.flake8"""
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
    """.flake8"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
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
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except MusicProduct.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
        covers = Cover.objects.all()
        cover = get_object_or_404(covers, page='checkout')

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'covers': covers,
        'cover': cover,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='checkout')
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'covers': covers,
        'cover': cover,
        'save_info': save_info,
    }

    return render(request, template, context)


@login_required
def checkout_lesson(request):
    """.git/"""
    lesson_bag = request.session.get('lesson_bag', {})
    if not lesson_bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('lessons'))

    current_bag = lesson_bag_contents(request)
    total = current_bag['lesson_total']
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='checkout')
    template = 'checkout/checkout_lesson.html'
    context = {
        'covers': covers,
        'cover': cover,
        'total': total,
    }

    return render(request, template, context)


@login_required
@csrf_exempt
def create_sub(request):
    """.git/"""
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Reads application/json and returns a response
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = settings.STRIPE_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)
        user = get_object_or_404(User, username=request.user)
        user_customer = user.customer
        if  user_customer is None:
            customer_exists = False
        else:
            customer_exists = True
        if customer_exists:
            try:
                customer_id = request.user.customer.id
                customer = stripe.Customer.retrieve(f'{customer_id}')

                # At this point, associate the ID of the Customer object with your
                # own internal representation of a customer, if you have one.
                # print(customer)

                # Subscribe the user to the subscription created
                subscription = stripe.Subscription.create(
                        customer=customer.id,
                        items=[
                            {
                                "price": data["price_id"],
                            },
                        ],
                        expand=["latest_invoice.payment_intent"]
                    )
                djstripe_subscription = (djstripe.models.Subscription.
                                         sync_from_stripe_data(subscription))
                try:
                    user_line_item = UserLineItem(
                        username=request.user,
                        subscription=djstripe_subscription,
                        subscription_user_id=djstripe_subscription.id,
                        subscription_name=djstripe_subscription.plan
                        )
                    user_line_item.save()
                    request.user.save()
                    username=request.user
                except username.DoesNotExist:
                    messages.error(request, (
                        "The user wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    subscription.delete()
                return JsonResponse(subscription)
            except Exception as e_rr:
                return JsonResponse({'error': (e_rr.args[0])}, status =403)
        else:
            try:
                # This creates a new Customer and attaches the PaymentMethod in one API call.
                customer = stripe.Customer.create(
                     payment_method=payment_method,
                     email=request.user.email,
                     name=request.user.get_full_name(),
                     phone=profile.default_phone_number,
                     address={
                         "city": profile.default_town_or_city,
                         "country": profile.default_country,
                         "line1": profile.default_street_address1,
                         "line2": profile.default_street_address2,
                         "postal_code": profile.default_postcode,
                         "state": profile.default_county
                         },
                     shipping={
                         "name":request.user.get_full_name(),
                         "phone":profile.default_phone_number,
                         "address": {
                             "city": profile.default_town_or_city,
                             "country": profile.default_country,
                             "line1": profile.default_street_address1,
                             "line2": profile.default_street_address2,
                             "postal_code": profile.default_postcode,
                             "state": profile.default_county
                         },},
                     invoice_settings={
                             'default_payment_method': payment_method}
                         )
                djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
                request.user.customer = djstripe_customer

                # At this point, associate the ID of the Customer object with your
                # own internal representation of a customer, if you have one.
                # print(customer)

                # Subscribe the user to the subscription created
                subscription = stripe.Subscription.create(
                    customer=customer,
                    items=[
                        {
                            "price": data["price_id"],
                        },
                    ],
                    expand=["latest_invoice.payment_intent"]
                )
                djstripe_subscription = (djstripe.models
                                         .Subscription.
                                         sync_from_stripe_data(subscription))

                try:
                    user_line_item = UserLineItem(
                        username=request.user,
                        subscription=djstripe_subscription,
                        subscription_user_id=djstripe_subscription.id,
                        subscription_name=djstripe_subscription.plan
                        )
                    user_line_item.save()
                    request.user.save()
                    username=request.user
                except username.DoesNotExist:
                    messages.error(request, (
                        "The user wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    subscription.delete()
                return JsonResponse(subscription)
            except Exception as e_rr:
                return JsonResponse({'error': (e_rr.args[0])}, status =403)

    else:
        return HttpResponse('request method not allowed')


@login_required
def subscribe(request):
    """.git/"""

    if request.method == 'POST':
        lesson_bag = request.session.get('lesson_bag', {})
        customer_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                user_customer_id = request.user.customer.id
                customer_subscribed = (SubscribedCustomer
                                       .objects.get(subscribed_customer_id=user_customer_id))
                customer_exists = True
                break
            except SubscribedCustomer.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if customer_exists:
            subscription_form = SubscribedCustomerForm(request.POST, instance=customer_subscribed)
            current_bag = lesson_bag_contents(request)
            total = current_bag['lesson_total']
            if subscription_form.is_valid():
                subscription_internal = subscription_form.save(commit=False)
                subscription_internal.save()
                try:
                    userlineitem = UserLineItem.objects.filter(username=request.user).latest()
                    subscription_id=userlineitem.subscription.id
                    subscription_line_item = SubscriptionLineItem(
                        subscribed_id=subscription_id,
                        subscription=userlineitem.subscription,
                        subscription_name=userlineitem.subscription_name,
                        customer=subscription_internal,
                        price=total,
                        quantity = 1,
                        original_lesson_bag = json.dumps(lesson_bag)
                        )
                    subscription_line_item.save()
                    userlineitem = UserLineItem.objects.filter(username=request.user).latest()
                    sub_id=userlineitem.subscription.id
                    subscription=get_object_or_404(Subscription, id=sub_id)
                except subscription.DoesNotExist:
                    messages.error(request, (
                        "The subscription in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    subscription_internal.delete()
                    return redirect(reverse('view_lesson_bag'))
                return redirect(reverse('checkout_lesson_complete', args=[sub_id]))
            else:
                messages.error(request, 'There was an error with your form. \
                    Please double check your information.')
                return HttpResponse(status=400)
        else:
            customer = None
            try:
                form_data = {
                    'full_name': request.POST.get('full_name'),
                    'email': request.POST.get('email'),
                    'phone_number': request.POST.get('phone_number'),
                    'country': request.POST.get('country'),
                    'postcode': request.POST.get('postcode'),
                    'town_or_city': request.POST.get('town_or_city'),
                    'street_address1': request.POST.get('street_address1'),
                    'street_address2': request.POST.get('street_address2'),
                    'county': request.POST.get('county'),
                }
                subscription_form = SubscribedCustomerForm(form_data)
                userlineitem = UserLineItem.objects.filter(username=request.user).latest()
                sub_id = userlineitem.subscription.id
                profile = UserProfile.objects.get(user=request.user)
                current_bag = lesson_bag_contents(request)
                total = current_bag['lesson_total']
                subscription=userlineitem.subscription
                if subscription_form.is_valid():
                    subscription_internal = subscription_form.save(commit=False)
                    subscription_internal.customer = request.user.customer
                    subscription_internal.subscribed_customer_id = request.user.customer.id
                    subscription_internal.user_profile = profile
                    subscription_internal.save()
                    try:
                        subscription_line_item = SubscriptionLineItem(
                            subscribed_id=subscription.id,
                            subscription=subscription,
                            subscription_name=subscription.subscription_name,
                            customer=subscription_internal,
                            price=total,
                            quantity = 1,
                            original_lesson_bag = json.dumps(lesson_bag)
                            )
                        subscription_line_item.save()
                    except subscription.DoesNotExist:
                        messages.error(request, (
                        "The subscription in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                        )
                        subscription_internal.delete()
                        return redirect(reverse('view_lesson_bag'))
                    customer = subscription_internal
                    return redirect(reverse('checkout_lesson_complete', args=[sub_id]))

                else:
                    messages.error(request, 'There was an error with your form. \
                        Please double check your information.')
                    return HttpResponse(status=400)
            except Exception as e_rr:
                if customer:
                    customer.delete()
                return HttpResponse(
                    content=f'Request to subscribe customer received:| ERROR: {e_rr}',
                    status=500)
    else:
        lesson_bag = request.session.get('lesson_bag', {})
        if not lesson_bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('lessons'))
        current_bag = lesson_bag_contents(request)
        total = current_bag['lesson_total']
        userlineitem = UserLineItem.objects.filter(username=request.user).latest()
        sub_id = userlineitem.subscription.id
        profile = UserProfile.objects.get(user=request.user)
        subscription= userlineitem.subscription_name
        subscription_form = SubscribedCustomerForm()
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='subscriptions')

    context = {'covers': covers,
                'cover': cover,
                'total': total,
                'sub_id': sub_id,
                'subscription': subscription,
                'subscription_form': subscription_form
    }
    return render(request, "checkout/subscription.html", context)


def cancel(request):
    """.git/"""
    if request.user.is_authenticated:
        userlineitem = UserLineItem.objects.filter(username=request.user).latest()
        sub_id = userlineitem.subscription.id

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        stripe.Subscription.delete(sub_id)
    except Exception as e_rr:
        return JsonResponse({'error': (e_rr.args[0])}, status =403)


    return redirect("home")

def checkout_lesson_complete(request, sub_id):
    """
    Handle successful checkouts
    """
    customer = request.user.customer
    subscribed_customer = get_object_or_404(SubscribedCustomer, subscribed_customer_id=customer.id)
    subscription_item = get_object_or_404(SubscriptionLineItem, subscribed_id=sub_id)
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='checkout')
    messages.success(request, f'Subscription successfully processed! \
        Your subscription number is {sub_id}. A confirmation \
        email will be sent to {subscribed_customer.email}.')

    if 'lesson_bag' in request.session:
        del request.session['lesson_bag']

    template = 'checkout/checkout_lesson_complete.html'
    context = {
        'subscribed_customer': subscribed_customer,
        'subscription_item': subscription_item,
        'sub_id': sub_id,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context)
