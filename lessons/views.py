""".git/"""
import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404,  redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from home.models import Cover
from .models import Lesson, Subscription, SubscribedUser
from .forms import SubscriptionForm


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
    subscription_forty_five = get_object_or_404(subscriptions,
                                                name='Weekly Payment - 45 minute lesson')
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
    subscriptions = Subscription.objects.all()
    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'lesson': request.POST['lesson'],
            'subscription_type': request.POST['subscription_type'],
            'quantity': request.POST['quantity'],
        }
        subscription_form = SubscriptionForm(form_data)
        if subscription_form.is_valid():
            subscription = subscription_form.save(commit=False)
            subscription.save()
            p_k = subscription.pk

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('subscription_confirmation', args=[p_k]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        subscription_form = SubscriptionForm()
        if request.user.is_authenticated:
            subscription_form = SubscriptionForm(initial={'full_name': request.user.get_full_name(),
                                            'email': request.user.email})
        else:
            subscription_form = SubscriptionForm()

    context = { 'covers': covers,
                'cover': cover,
                'subscriptions': subscriptions,
                'subscription_form': subscription_form}

    return render(request, 'lessons/subscriptions.html', context)


def subscription_confirmation(request, p_k):
    """.git/"""
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='subscriptions')
    subscriptions = Subscription.objects.all()
    subscribed_users = SubscribedUser.objects.all()
    subscription = get_object_or_404(subscribed_users, pk=p_k)
    full_name = subscription.full_name
    email = subscription.email
    lesson = subscription.lesson
    subscription_type = subscription.subscription_type
    subscription_types = subscription_type
    selected_quantity = subscription.quantity
    selected_price = 0.00
    quoted_price = 0.00
    subscription_thirty = get_object_or_404(subscriptions, name='Weekly Payment - 30 minute lesson')
    subscription_forty_five = get_object_or_404(subscriptions,
                                                 name='Weekly Payment - 45 minute lesson')
    subscription_thirty_monthly = get_object_or_404(subscriptions,
                                                 name='Monthly Payment - 30 minute lesson')
    subscription_forty_five_monthly = get_object_or_404(subscriptions,
                                                 name='Monthly Payment - 45 minute lesson')
    subscription_thirty_annual = get_object_or_404(subscriptions,
                                                 name='Annual Payment - 30 minute lesson')
    subscription_forty_five_annual = get_object_or_404(subscriptions,
                                                 name='Annual Payment - 45 minute lesson')
    if subscription_types == subscription_thirty:
        selected_price = settings.STRIPE_PRICE_ID_WEEKLY_30
        quoted_price = subscription_thirty.price
    elif subscription_types == subscription_forty_five:
        selected_price = settings.STRIPE_PRICE_ID_WEEKLY_45
        quoted_price = subscription_forty_five.price
    elif subscription_types == subscription_thirty_monthly:
        selected_price = settings.STRIPE_PRICE_ID_MONTHLY_30
        quoted_price = subscription_thirty_monthly.price
    elif subscription_types == subscription_forty_five_monthly:
        selected_price = settings.STRIPE_PRICE_ID_MONTHLY_45
        quoted_price = subscription_forty_five_monthly.price
    elif subscription_types == subscription_thirty_annual:
        selected_price = settings.STRIPE_PRICE_ID_ANNUAL_30
        quoted_price = subscription_thirty_annual.price
    elif subscription_types == subscription_forty_five_annual:
        selected_price = settings.STRIPE_PRICE_ID_ANNUAL_45
        quoted_price = subscription_forty_five_annual.price
    else:
        messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    context = { 'covers': covers,
                'cover': cover,
                'full_name': full_name,
                'email': email,
                'lesson': lesson,
                'subscription_types': subscription_types,
                'selected_quantity': selected_quantity,
                'selected_price': selected_price,
                'quoted_price': quoted_price}

    return render(request, 'lessons/subscription_confirmation.html', context)



@csrf_exempt
def stripe_configuration(request, p_k):
    """.git/"""
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request, p_k):
    """.git/"""
    subscriptions = Subscription.objects.all()
    subscribed_users = SubscribedUser.objects.all()
    subscription = get_object_or_404(subscribed_users, pk=p_k)
    full_name = subscription.full_name
    email = subscription.email
    subscription_type = subscription.subscription_type
    subscription_types = subscription_type
    selected_quantity = subscription.quantity
    selected_price = 0.00
    subscription_thirty = get_object_or_404(subscriptions, name='Weekly Payment - 30 minute lesson')
    subscription_forty_five = get_object_or_404(subscriptions,
                                                 name='Weekly Payment - 45 minute lesson')
    subscription_thirty_monthly = get_object_or_404(subscriptions,
                                                 name='Monthly Payment - 30 minute lesson')
    subscription_forty_five_monthly = get_object_or_404(subscriptions,
                                                 name='Monthly Payment - 45 minute lesson')
    subscription_thirty_annual = get_object_or_404(subscriptions,
                                                 name='Annual Payment - 30 minute lesson')
    subscription_forty_five_annual = get_object_or_404(subscriptions,
                                                 name='Annual Payment - 45 minute lesson')
    if subscription_types == subscription_thirty:
        selected_price = settings.STRIPE_PRICE_ID_WEEKLY_30
    elif subscription_types == subscription_forty_five:
        selected_price = settings.STRIPE_PRICE_ID_WEEKLY_45
    elif subscription_types == subscription_thirty_monthly:
        selected_price = settings.STRIPE_PRICE_ID_MONTHLY_30
    elif subscription_types == subscription_forty_five_monthly:
        selected_price = settings.STRIPE_PRICE_ID_MONTHLY_45
    elif subscription_types == subscription_thirty_annual:
        selected_price = settings.STRIPE_PRICE_ID_ANNUAL_30
    elif subscription_types == subscription_forty_five_annual:
        selected_price = settings.STRIPE_PRICE_ID_ANNUAL_45
    else:
        messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    if request.method == 'GET':
        domain_url = 'https://8000-clairepotter-bellemusiqu-5d6cp7e00lc.ws-eu34.gitpod.io/'
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
                        'price': selected_price,
                        'quantity': selected_quantity,
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
