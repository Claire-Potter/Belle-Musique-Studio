"""
xxx
"""
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from home.models import Cover
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='account_profile')
    context = { 'covers': covers,
                'cover': cover,
                'form': form,
                'orders': orders,
                'on_profile_page': True}

    return render(request, template, context)
