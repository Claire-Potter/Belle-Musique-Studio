""".git/"""
import json

import djstripe
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from djstripe.models import Product
from profiles.models import UserProfile

from home.models import Cover

from .models import Lesson, SubscribedCustomer


def lessons_details(request):
    """ A view to show the lessons page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')
    lessons = Lesson.objects.all()
    context = {'covers': covers,
                'cover': cover,
                'lessons': lessons,
              }

    return render(request, 'lessons/lessons.html', context)


@login_required
def subscriptions_details(request):
    """ A view to show the lessons page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='subscriptions')
    products = Product.objects.all()
    context = {'covers': covers,
                'cover': cover,
                'products': products,}
    return render(request, 'lessons/subscriptions.html', context)


@login_required
@csrf_exempt
def create_sub(request):
    """.git/"""
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Reads application/json and returns a response
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = settings.STRIPE_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)

        try:
            # This creates a new Customer and attaches the PaymentMethod in one API call.
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.user.email,
                name=request.user.get_full_name(),
                phone=profile.default_phone_number,
                shipping={
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
                customer=customer.id,
                items=[
                    {
                        "price": data["price_id"],
                    },
                ],
                expand=["latest_invoice.payment_intent"]
            )

            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

            request.user.subscription = djstripe_subscription
            request.user.save()

            return JsonResponse(subscription)
        except Exception as e_rr:
            return JsonResponse({'error': (e_rr.args[0])}, status =403)
    else:
        return HttpResponse('request method not allowed')


def complete(request):
    """.git/"""
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='subscriptions')
    products = Product.objects.all()
    context = {'covers': covers,
                'cover': cover,
                'products': products,}
    return render(request, "lessons/complete.html", context)


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
