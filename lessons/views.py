""".git/"""
import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import Cover
from .models import Lesson, Subscription


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
    subscriptions = Subscription.objects.all()
    subscription_thirty = get_object_or_404(subscriptions, name='Weekly Payment - 30 minute lesson')
    subscription_forty_five = get_object_or_404(subscriptions, name='Weekly Payment - 45 minute lesson')
    context = { 'covers': covers,
                'cover': cover,
                'piano_lessons': piano_lessons,
                'piano_lesson_image': piano_lesson_image,
                'singing_lessons': singing_lessons,
                'singing_lesson_image': singing_lesson_image,
                'song_lessons': song_lessons,
                'song_lesson_image': song_lesson_image,
                'subscription_thirty': subscription_thirty,
                'subscription_forty_five': subscription_forty_five}

    return render(request, 'lessons/lessons.html', context)


@login_required
def subscriptions_details(request):
    """ A view to show the lessons page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='subscriptions')
    context = { 'covers': covers,
                'cover': cover}

    return render(request, 'lessons/subscriptions.html', context)


@csrf_exempt
def stripe_configuration(request):
    """.git/"""
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    """.git/"""
    if request.method == 'GET':
        domain_url = 'https://8000-clairepotter-bellemusiqu-nsq454enhwj.ws-eu31.gitpod.io/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'lessons/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'lessons/cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID_WEEKLY_30,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def success(request):
    return render(request, 'lessons/success.html')


@login_required
def cancel(request):
    return render(request, 'lessons/cancel.html')
