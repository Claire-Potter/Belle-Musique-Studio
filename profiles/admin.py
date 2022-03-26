"""
Belle Musique Studio profiles app admin configuration

Definitions from https://www.fullstackpython.com
unless stated otherwise
"""
from django.contrib import admin
# The Django admin is an automatically-generated user interface for
# Django models. The admin interface can be heavily customized
from .models import UserProfile
# Models are imported from models.py


class UserProfileAdmin(admin.ModelAdmin):
    """
    The UserProfile admin set up reads the UserProfile model.

    The admin fields have been set up as read only, to protect the user's
    data and to ensure any updates are completed by the user themselves.
    """
    model = UserProfile

    readonly_fields = ('user', 'default_full_name', 'default_email',
                       'default_additional_email',
                       'default_phone_number', 'default_street_address1',
                       'default_street_address2',
                       'default_town_or_city', 'default_county',
                       'default_postcode',
                       'default_country',)
    list_display = ('user', 'default_full_name', 'default_email')


admin.site.register(UserProfile, UserProfileAdmin)
