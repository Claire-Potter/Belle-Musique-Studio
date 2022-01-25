"""
Belle Musique Studio home app views configuration
After correcting any pylint issues, I was still left with the issue
'class has no objects member', the object is only added when the screen
is  rendered in the browser, so the issue is not valid. I followed
the steps available for the following stack overflow:
https://stackoverflow.com/questions/45135263/class-has-no-objects-member
and created the .pylintrc file to customise the pylint settings to
prevent this error from displaying.
the index view is set up to display the homepage.
the social media views are set up to authorise login via the
various social media apps. This was completed as per the django
documentation:
https://django-rest-auth.readthedocs.io/en/latest/installation.html
Contact View created to render the Contact page.
The view also references the Contact model
and form in order to update the fields within
the model tables
"""

from django.shortcuts import render, get_object_or_404
from .models import Home


def index(request):
    """ A view to return the index page """
    queryset = Home.objects.all()
    home = get_object_or_404(queryset)

    context = {
        'home': home,
    }

    return render(request, 'index.html', context)


def about(request):
    """ A view to return the about page """

    return render(request, 'about.html')
