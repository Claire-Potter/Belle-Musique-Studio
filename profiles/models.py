"""
Belle Musique Studio profile app model configuration:

The UserProfile model allows the user to read, edit and
delete the various userprofile fields.
The model can be updated when an order is placed with order address details
added by the user.

Created as per the Code Institute 'Boutique Ado' project.

Definitions from https://www.fullstackpython.com
unless stated otherwise.

"""
from django.db import models
# models is a callable within the django.db module of the Django project.
from django.db.models.signals import post_save
# post_save is a callable within the django.db.models.signals module
# of the Django project.
from django.dispatch import receiver
# The Signal class allows certain senders to notify a set of receivers that
# some action
#  has taken place across Django apps within the same project.
from django_countries.fields import CountryField
# A Django application that provides country choices for use with forms,
# flag icons static files, and a country field for models.
# (https://pypi.org/project/django-countries/#:~:text=
# A%20Django%20application%20that%20provides,Installation)

from home.models import User
# Model is imported from home app models.py


class UserProfile(models.Model):
    """
    The UserProfile  model allows the user to read,
    edit and delete the various userprofile fields.
    The model can be updated when an order is placed with
    order address details
    added by the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(default='', max_length=50,
                                         null=True, blank=True)
    default_email = models.EmailField(default='', max_length=254,
                                      null=True, blank=True)
    default_additional_email = models.EmailField(default='', max_length=254,
                                                 null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_county = models.CharField(max_length=80, null=True,
                                      blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
    instance.userprofile.save()
