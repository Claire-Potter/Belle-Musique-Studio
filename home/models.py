"""
Belle Musique Studio home app model configuration:

The User model replaces the allauth default User. It is
used to create User accounts to authenticate and access the site.

The User Subscription model is utilised to link djstripe Subscriptions to a
User record when the record is created in Stripe.

The Contact model created to render the contact page
and to store all contact requests submitted by users and non-users.

The Cover model is utilised to store the unique page titles and quotes for different
site sections.

The StudentShowcase model is utilised to add the details of a student who the staff have chosen
to showcase. Once saved, the latest record displays on the About page.

SuperUser can access all models from the Site Admin page.
Admin provided necessary access only.

Definitions from https://www.fullstackpython.com
unless stated otherwise.

"""
from django.contrib.auth.models import AbstractUser
# Abstract User:
# If you’re starting a new project, it’s highly recommended to set up a custom user model,
# even if the default User model is sufficient for you. This model behaves identically to the
# default user model, but you’ll be able to customize it in the future if the need arises.
# Don’t forget to point AUTH_USER_MODEL to it. Do this before creating any migrations or running
# manage.py migrate for the first time. Also, register the model in the app’s admin.py.
# definition from https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
from django.db import models
# models is a callable within the django.db module of the Django project.
from embed_video.fields import EmbedVideoField
# Django app for easy embedding YouTube and Vimeo videos and music from SoundCloud.
# definition from https://pypi.org/project/django-embed-video/
from djstripe.models import Customer, Subscription
# dj-stripe implements all of the Stripe models, for Django.
# definition from https://pypi.org/project/dj-stripe/


class User(AbstractUser):
    """
    The User model replaces the allauth default User. It is
    used to create User accounts to authenticate and access the site.
    The customer field is used to store the associated Stripe customer once
    they have been created and returned from Stripe.com.

    Set up as per https://ordinarycoders.com/blog/article/django-stripe-monthly-subscription
    and customised.
    """
    customer = models.OneToOneField(Customer, null=True, blank=True, on_delete=models.CASCADE)


class UserSubscription(models.Model):
    """
    The User Subscription model is utilised to link djstripe Subscriptions to a
    User record when the record is created in Stripe. A Foreign key field is 
    used to link the model to the parent User model.
    """
    username = models.ForeignKey(User, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='userlineitems',
                              editable=False)
    subscription_user_id = models.CharField(max_length=350, unique=True, null=True, blank=True,
                                             editable=False)
    subscription_name = models.CharField(max_length=350, null=True, blank=True,
                                          editable=False)
    subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL,
                                     editable=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        """
        Meta created to order the UserSubscription model by date
        and to return the most recent field according to date.
        """
        ordering = ['date']
        get_latest_by = ['date']


    def __str__(self):
        return f'{self.subscription}'


class Contact(models.Model):
    """
    Model created to render the contact page
    and save the contact request data.
    """
    username = models.ForeignKey(User, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='contact')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta created to order the Contact Model according
        to the created on date.
        """
        ordering = ['-created_on']
        verbose_name_plural = 'Contact Requests'

    def __str__(self):
        return f'Contact request {self.body} by {self.name}'


class Cover(models.Model):
    """
    Model created to render the cover input
    and save the cover name and quote to reflect.
    """
    name = models.CharField(max_length=80)
    quote = models.CharField(max_length=250)
    page = models.CharField(max_length=15, default='home')

    class Meta:
        """
        Meta created to order the Cover Model according
        to the page.
        """
        ordering = ['page']

    # The string is set to return the name and quote fields
    def __str__(self):
        return f'Cover details: {self.name} and {self.quote}'


class StudentShowcase(models.Model):
    """
    Utilised to store the data added to create a student showcase record.
    Data is captured via the Add Student Showcase front end page or in Site Admin.
    Each record added should be linked back to the associated Stripe customer and 
    subscription for record keeping purposes.
    """
    name = models.CharField(max_length=80, unique=True,
                             default='placeholder')
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    video_name = models.CharField(max_length=100, blank=True,
                                  default='placeholder')
    video_url = EmbedVideoField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,
                              on_delete=models.CASCADE, related_name='showcase_customer')
    subscription = models.ForeignKey(Subscription,
                              on_delete=models.CASCADE, related_name='showcase_subscription')



    class Meta:
        """
        Meta created to order the Student Showcase Model according
        to date, to return the latest record according to date and
        to set the admin model name to Student Showcase.
        """
        ordering = ['date']
        verbose_name_plural = 'Student Showcase'
        get_latest_by = ['date']

    # The string is set to return the name field if it exists
    #  else a blank string
    def __str__(self):
        return '%s' % (self.name) if self.name else ' '
