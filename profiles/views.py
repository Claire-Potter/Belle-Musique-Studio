"""
xxx
"""
from django.shortcuts import render, get_object_or_404
from home.models import Cover


def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='account_profile')
    context = { 'covers': covers,
                'cover': cover}

    return render(request, template, context)
