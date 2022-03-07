""".git/"""
import json

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

from home.models import Cover
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from shopping_bag.contexts import bag_contents, lesson_bag_contents
from store.models import MusicProduct

from .forms import OrderForm, SubscribedCustomerForm
from .models import Order, OrderLineItem, SubscribedCustomer, SubscriptionLineItem


@require_POST
def cache_checkout_data(request):
    """.git/"""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@require_POST
def cache_checkout_data_lesson(request):
    """.git/"""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'lesson_bag': json.dumps(request.session.get('lesson_bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """.git/"""
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

        if request.user.is_authenticated:
            order_form = OrderForm(initial={'full_name': request.user.get_full_name(),
                                            'email': request.user.email})
        else:
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
        'stripe_secret_key': stripe_secret_key,
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

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

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
@csrf_exempt
def checkout_lesson(request):
    """.git/"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        lesson_bag = request.session.get('lesson_bag', {})
         # Reads application/json and returns a response
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = settings.STRIPE_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)

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
        try:
             customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.POST['email'],
                name=request.POST['full_name'],
                phone=request.POST['phone_number'],
                shipping={
                    "name":request.POST['full_name'],
                    "address": {
                "city": request.POST['town_or_city'],
                "country": request.POST['country'],
                "line1": request.POST['street_address1'],
                "line2": request.POST['street_address2'],
                "postal_code": request.POST['postcode'],
                "state": request.POST['county']
              },},
                invoice_settings={
                    'default_payment_method': payment_method}
                    )

             djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
             customer = djstripe_customer

             # This creates a new Customer and attaches the PaymentMethod in one API call.
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

             djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

             subscription = djstripe_subscription
             subscription_form = SubscribedCustomerForm(form_data)
             if subscription_form.is_valid():
                 subscription_internal = subscription_form.save(commit=False)
                 subscription_internal.original_lesson_bag = json.dumps(lesson_bag)
                 subscription_internal.save()
                 for lesson_id, lesson_data in lesson_bag.items():
                     try:

                         if isinstance(lesson_data, int):
                             price_only = lesson_data[0]
                             priceId = lesson_data[1]
                             name = lesson_data[2]
                             price = lesson_data[3]
                             url = lesson_data[4]
                             caption = lesson_data[5]
                             subscription_line_item = SubscriptionLineItem(
                                 subscription=subscription,
                                 customer=customer,
                                 quantity=1,
                                 price=price_only,
                                 lineitem_total=price_only,
                            
                             ) 
                             subscription_line_item.save()
                         else:
                             price_only = lesson_data[0]
                             priceId = lesson_data[1]
                             name = lesson_data[2]
                             price = lesson_data[3]
                             url = lesson_data[4]
                             caption = lesson_data[5]
                             subscription_line_item = SubscriptionLineItem(
                                 subscription=subscription,
                                 customer=customer,
                                 quantity=1,
                                 price=price_only,
                                 lineitem_total=price_only,
                            
                             )
                             subscription_line_item.save()
                     except lesson_bag.DoesNotExist:
                         messages.error(request, (
                             "Your subscription wasn't found. "
                             "Please call us for assistance!")
                         )
                         subscription.delete()
                         return redirect(reverse('view_lesson_bag'))

                 request.session['save_info'] = 'save-info' in request.POST
                 return redirect(reverse('checkout_lesson_success', args=[subscription]))
             else:
                 messages.error(request, 'There was an error with your form. \
                    Please double check your information.')
            

             return JsonResponse(subscription)
        except Exception as e_rr:
            return JsonResponse({'error': (e_rr.args[0])}, status =403) 
    else:
        lesson_bag = request.session.get('lesson_bag', {})
        if not lesson_bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('lessons'))

        current_bag = lesson_bag_contents(request)
        total = current_bag['lesson_total']

        if request.user.is_authenticated:
            subscription_form = SubscribedCustomerForm(initial={'full_name': request.user.get_full_name(),
                                            'email': request.user.email})
        else:
            subscription_form = SubscribedCustomerForm()
        covers = Cover.objects.all()
        cover = get_object_or_404(covers, page='checkout')

    template = 'checkout/checkout_lesson.html'
    context = {
        'subscription_form': subscription_form,
        'covers': covers,
        'cover': cover,
        'stripe_public_key': stripe_public_key,
    }

    return render(request, template, context)


def checkout_lesson_success(request):
    """.git/"""
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='subscriptions')
    context = {'covers': covers,
    'cover': cover,}
    return render(request, "checkout/complete.html", context)


def cancel(request):
    """.git/"""
    if request.user.is_authenticated:
        sub_id = request.user.subscription.id

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        stripe.Subscription.delete(sub_id)
    except Exception as e_rr:
        return JsonResponse({'error': (e_rr.args[0])}, status =403)


    return redirect("home")
