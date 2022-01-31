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

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from .forms import ContactForm
from .models import User


def index(request):
    """ A view to return the index page """

    return render(request, 'index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'about.html')


class Contact(View):
    """
    View created to render the Contact page.
    The view also references the Contact model
    and form in order to update the fields within
    the model tables
    """

    def get(self, request):
        """
        The get function retrieves the data
        to generate the contact page.
        self: The self is used to represent the instance of the class.
        request: The requests module allows you to send HTTP
        requests using Python.The HTTP request returns a Response
        Object with all the response data (content, encoding, status, etc).
        Definition from https://www.w3schools.com/python/module_requests.asp
        If and else statement utilised to determine whether the user
        is logged in or not, if they are logged in, their name and email
        address will be derived from their user profile.
        """
        if User.objects.filter(username=self.request.user.username).exists():
            contact_form = ContactForm(initial={'name': request.user.username,
                                                'email': request.user.email})
        else:
            contact_form = ContactForm()
        return render(
            request,
            'contact.html',
            {
                'contact_form': contact_form,
            },
        )

    def post(self, request):
        """
        self: The self is used to represent the instance of the class.
        request: The requests module allows you to send HTTP
        requests using Python.The HTTP request returns a Response
        Object with all the response data (content, encoding, status, etc).
        Definition from https://www.w3schools.com/python/module_requests.asp
        If and else statement utilised to determine whether the user
        is logged in or not, if they are logged in, their name and email
        address will be derived from their user profile.
        Set up according to django EmailMultiAlternatives
        https://docs.djangoproject.com/en/4.0/topics/email/
        and include Sendgrid email template
        """

        # check if form has been submitted
        if request.method == 'POST':
            # check if data from the form is clean
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.save()
                c_d = contact_form.cleaned_data
                text_content = c_d['body']
                client_name = c_d['name']
                client_email = c_d['email']
                subject = 'A new Request has been submitted'
                message = f'Contact request {text_content} by {client_name} @ {client_email}'
                recipient = 'bellemusiquestudio@gmail.com'
                email_from = settings.EMAIL_HOST_USER

                # send the email to the recipient
                send_mail(subject,
                          message,
                          email_from, [recipient], fail_silently = False)

                return redirect('contact-sent')

            else:
                contact_form = ContactForm()

            return render(
                request,
                'contact.html',
                {
                   'contact_form': contact_form,

                },
            )


def contact_sent(request):
    """ A view to return the contact sent page """

    return render(request, 'contact_sent.html')
