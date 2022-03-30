"""
Belle Musique Studio home app admin configuration

Definitions from https://www.fullstackpython.com
unless stated otherwise
"""
from django.contrib import admin
# The Django admin is an automatically-generated user interface for
# Django models. The admin interface can be heavily customized
from embed_video.admin import AdminVideoMixin
# Django app for easy embedding YouTube and Vimeo videos and
# music from SoundCloud.
# definition from https://pypi.org/project/django-embed-video/
from .models import (Contact, Cover, User, UserSubscription, StudentShowcase,
                     MarketingSignUp)
# Models are imported from models.py


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    The Contact admin set up reads the Contact model and allows
    the admin user to read and delete contact requests.
    """
    list_display = ('name', 'email', 'created_on')
    list_filter = ('created_on', 'name')
    search_fields = ('name', 'email')


@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):
    """
    The Cover admin set up reads the Cover model and allows
    the admin user to read, edit and delete input for the cover
    name and cover quotes
    used across the site.
    """
    list_display = ('name', 'quote', 'page')
    list_filter = ('name', 'quote', 'page')
    search_fields = ('name', 'quote', 'page')


class UserSubscriptionAdmin(admin.ModelAdmin):
    """
    The UserSubscription admin set up reads the UserSubscription model.
    It allows the user to readonly the subscription information linked
    to the username. The records within the model are created through the
    djstripe integration.
    """
    model = UserSubscription
    readonly_fields = ('subscription_user_id', 'subscription_name',
                       'username', 'date')
    list_display = ('subscription_user_id', 'subscription_name',
                    'username', 'date')
    search_fields = ('subscription_user_id', 'subscription_name', 'date')


    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(UserSubscription, UserSubscriptionAdmin)


class UserAdmin(admin.ModelAdmin):
    """
    The User admin set up reads the customised User model.
    It allows the user to read, edit and delete the various user fields.
    The customer field is created by djstripe when a customer
    record is created.
    """
    model = User
    readonly_fields = ('customer',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(User, UserAdmin)


@admin.register(StudentShowcase)
class StudentShowcaseAdmin(AdminVideoMixin,
                           admin.ModelAdmin):
    """
    The StudentShowcase admin set up reads the StudentShowcase model and allows
    the admin user to create a new record by adding the
    required fields. Admin can also edit and delete.
    Embed video field is used to save videos and display them
    in the admin pane.
    """
    list_display = ('date', 'name',)
    search_fields = ['date', 'name', ]


@admin.register(MarketingSignUp)
class MarketingSignUpAdmin(admin.ModelAdmin):
    """
    The MarketingSignUp admin set up reads the MarketingSignUp model and allows
    the admin user to view all site users who have opted in to receive the
    newsletter
    """
    list_display = ('date', 'email',)
    search_fields = ['date', 'email', ]
