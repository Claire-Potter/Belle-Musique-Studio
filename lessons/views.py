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

from home.models import Cover

from .models import Lesson


def lessons_details(request):
    """ A view to show the lessons page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')
    piano_lessons = Lesson.objects.filter(type=1)
    piano_lesson_image = get_object_or_404(piano_lessons,
                                           image_description='A young girl playing the piano')
    singing_lessons = Lesson.objects.filter(type=2)
    singing_lesson_image = get_object_or_404(singing_lessons,
                                             image_description='A young boy'
                                                               ' singing into a microphone')
    song_lessons = Lesson.objects.filter(type=3)
    song_lesson_image = get_object_or_404(song_lessons,
                                          image_description='A woman playing the piano and singing')
    context = {'covers': covers,
                'cover': cover,
                'piano_lessons': piano_lessons,
                'piano_lesson_image': piano_lesson_image,
                'singing_lessons': singing_lessons,
                'singing_lesson_image': singing_lesson_image,
                'song_lessons': song_lessons,
                'song_lesson_image': song_lesson_image,}

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
