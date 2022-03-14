"""
xxx
"""
from django.contrib import messages
from django.shortcuts import get_object_or_404, render

from checkout.models import Order
from home.models import Cover

from .forms import UserProfileForm
from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile, initial={'default_full_name': request.user.get_full_name(),
            'default_email': request.user.email,})
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='account_profile')
    context = {'covers': covers,
                'cover': cover,
                'form': form,
                'orders': orders,
                'on_profile_page': True}

    return render(request, template, context)


def order_history(request, order_number):
    """.git/"""
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
