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

the privacy view is a view to return the privacy policy.

the About view is set up to display the about page.

Contact View created to render the Contact page.
The view also references the Contact model
and form in order to update the fields within
the model tables.

Contact sent view rendered once a contact sent request has been
successfully submitted and sent.

Student showcase view utilised to render the form within which
admin can capture the information of the student to be showcased.

Messages definition from:
https://docs.djangoproject.com/en/4.0/ref/contrib/messages/

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""

from django.conf import settings
# The Django settings file contains all of the configuration for
# a web application.
from django.core.mail import send_mail
# send_mail is a function in Django that can send an email using the
# EmailMessage class.
from django.core import mail
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
# render_to_string is a callable within the django.template.loader
# module of the Django project.
from django.contrib import messages
# Quite commonly in web applications, you need to display a one-time
# notification
# message (also known as “flash message”) to the user after processing
# a form or
#  some other types of user input.

# For this, Django provides full support for cookie- and session-based
# messaging,
# for both anonymous and authenticated users. The messages framework allows you
# to temporarily store messages in one request and retrieve them for
# display in a
# subsequent request (usually the next one). Every message is
# tagged with a specific level
# that determines its priority (e.g., info, warning, or error).

from django.contrib.auth.decorators import login_required
# @login_required: Django's login_required function is used to secure views
# in your web applications by forcing the client to
# authenticate with a valid logged-in User.
from django.shortcuts import get_object_or_404, redirect, render, reverse
# get_object_or_404 is a callable within the django.shortcuts module
# of the Django project.
# redirect is a callable within the django.shortcuts module of the
# Django project.
# render is a callable within the django.shortcuts module of the
# Django project.
# reverse is a callable within the django.urls module of the Django project.
from django.views import View
# View is a class within the django.views.generic module of the Django project.
from .forms import ContactForm, StudentShowcaseForm, NewsLetterForm
# Forms are imported from forms.py
from .models import Cover, User, StudentShowcase, MarketingSignUp
# Models are imported from models.py


def index(request):
    """
    A view to return the home page as index.html

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp
    """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='home')
    context = {'covers': covers,
               'cover': cover}

    return render(request, 'index.html', context)


def privacy(request):
    """
    A view to return the privacy policy

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp
    """

    return render(request, 'privacy_policy.html')


def about(request):
    """
    A view to return the About page.
    This contains the information about who Belle Musique Studio are,
    who the owner is, high level information about lessons, the
    student showcase
    section and links to the various products in the music store.

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp
    """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='about')
    student_showcased = StudentShowcase.objects.latest()
    context = {'covers': covers,
               'cover': cover,
               'student_showcased': student_showcased}

    return render(request, 'about.html', context)


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
        requests using Python.
        The HTTP request returns a Response
        Object with all the response data (content, encoding, status, etc).

        Definition from https://www.w3schools.com/python/module_requests.asp

        If and else statement utilised to determine whether the user
        is logged in or not, if they are logged in, their name and email
        address will be derived from their user profile.
        """
        if User.objects.filter(username=self.request.user.username).exists():
            contact_form = ContactForm(initial={'name': (request.user
                                                         .get_full_name()),
                                                'email': request.user.email})
        else:
            contact_form = ContactForm()
        covers = Cover.objects.all()
        cover = get_object_or_404(covers, page='contact')
        context = {'covers': covers,
                   'cover': cover,
                   'contact_form': contact_form, }
        return render(
            request,
            'contact.html', context)

    def post(self, request):
        """
        self: The self is used to represent the instance of the class.
        request: The requests module allows you to send HTTP
        requests using Python.
        The HTTP request returns a Response
        Object with all the response data (content, encoding, status, etc).

        Definition from https://www.w3schools.com/python/module_requests.asp

        If and else statement utilised to determine whether the user
        is logged in or not, if they are logged in, their name and email
        address will be derived from their user profile.

        """
        # check if form has been submitted
        if request.method == 'POST':
            # check if data from the form is clean
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                if (User.objects.filter(username=self.
                                        request.user.username).exists()):
                    contact.username = request.user
                contact.save()
                c_d = contact_form.cleaned_data
                text_content = c_d['body']
                client_name = c_d['name']
                client_email = c_d['email']
                subject = 'A new Request has been submitted'
                message = f'Contact request {text_content} by {client_name} \
                @ {client_email}'
                recipient = 'bellemusiquestudio@gmail.com'
                email_from = settings.EMAIL_HOST_USER

                # send the email to the recipient
                send_mail(subject,
                          message,
                          email_from, [recipient], fail_silently=False)

                return redirect('contact-sent')

            else:
                contact_form = ContactForm()
            covers = Cover.objects.all()
            cover = get_object_or_404(covers, page='contact')
            context = {'covers': covers,
                       'cover': cover,
                       'contact_form': contact_form, }
            return render(
                request,
                'contact.html', context)


def contact_sent(request):
    """
    A view to return the contact sent page
    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp
     """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='contact')
    context = {'covers': covers,
               'cover': cover}

    return render(request, 'contact_sent.html', context)


@login_required
def add_student_showcase(request):
    """
    Add a student to be showcased on the about page.

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp

    The StudentShowcaseForm is rendered on the page to allow admin to
    capture student information from the front end. Once saved it
    is created as a record within the StudentShowcase model.
    The most recent record is called and displayed
    on the About page.

    If statement is utilised to determine if the user is a staff member, if not
    they will be denied access.
    If and else statement utilised to determine whether the request
    is a post or not, if not, the form without content
    will be rendered for the user to complete,
    if it is 'POST' the completed form will be requested and saved.
    An If and else statement is utilised to check for errors, if
    successful a success
    message will display, if not an error message will display.
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = StudentShowcaseForm(request.POST)
        if form.is_valid():
            form.save()
            connection = mail.get_connection()
            connection.open()
            email_messages = list()
            marketing_users = MarketingSignUp.objects.all()
            for u in marketing_users:
                first_name =  u.first_name
                events = StudentShowcase.objects.latest()
                event = events.name
                subject =  render_to_string('showcase_email/showcase_email_subject.txt',
                                            {'event': event})
                from_email = settings.DEFAULT_FROM_EMAIL
                to = u.email
                body = render_to_string('showcase_email/showcase_email_body.txt',
                                 {'event': event, 
                                  'contact_email': settings.DEFAULT_FROM_EMAIL, 'first_name': first_name})
                msg = EmailMultiAlternatives(subject, body, from_email, [to])
                email_messages.append(msg)
            connection.send_messages(email_messages)
            connection.close()
            messages.success(request, 'Successfully added '
                             'new student showcase!')
            return redirect(reverse('home'))
        else:
            messages.error(request,
                           ('Failed to add student showcase. '
                            'Please ensure the form is valid.'))
    else:
        form = StudentShowcaseForm()
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='student_comm')
    template = 'add_student_showcase.html'
    context = {
        'form': form,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context)


def marketing_newsletter_sign_up(request):
    """
    Allows site users to sign up to receive a marketing newsletter

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp

   """
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added '
                             'you to our newsletter recipient list!')
            return redirect(reverse('home'))
        else:
            messages.error(request,
                           ('Failed to add you to our newsletter list. '
                            'Please ensure the form is valid.'))
    else:
        if User.objects.filter(username=request.user.username).exists():
            form = NewsLetterForm(initial={'first_name': (request.user
                                                    .first_name),
                                           'last_name': (request.user
                                                    .last_name),
                                           'email': request.user.email})
        else:
            form = NewsLetterForm()
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='about')
    template = 'marketing_sign_up.html'
    context = {
        'form': form,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context)

