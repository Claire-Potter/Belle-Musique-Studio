"""
Belle Musique Studio home app admin configuration

Definitions from https://www.fullstackpython.com
unless stated otherwise
"""
from django.contrib import admin
# The Django admin is an automatically-generated user interface for
# Django models. The admin interface can be heavily customized
from django_summernote.admin import SummernoteModelAdmin
# Summernote is a simple WYSIWYG editor.
# django-summernote allows you to embed Summernote into Django
#  very handy. Support admin mixins and widgets.
# definition from https://github.com/summernote/django-summernote
from embed_video.admin import AdminVideoMixin
# Django app for easy embedding YouTube and Vimeo videos and
# music from SoundCloud.
# definition from https://pypi.org/project/django-embed-video/
from .models import Contact, Cover, User, UserSubscription, StudentShowcase
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


admin.site.register(UserSubscription, UserSubscriptionAdmin)


class UserAdmin(admin.ModelAdmin):
    """
    The User admin set up reads the customised User model.
    It allows the user to read, edit and delete the various user fields.
    The customer field is created by djstripe when a customer
    record is created.
    """
    model = User


admin.site.register(User, UserAdmin)


@admin.register(StudentShowcase)
class StudentShowcaseAdmin(SummernoteModelAdmin, AdminVideoMixin,
                           admin.ModelAdmin):
    """
    The StudentShowcase admin set up reads the StudentShowcase model and allows
    the admin user to create a new record by adding the
    required fields. Admin can also edit and delete.
    Django summernote is included to allow the admin user
    to style the body field.
    Embed video field is used to save videos and display them
    in the admin pane.
    """
    list_display = ('date', 'name',)
    search_fields = ['date', 'name', ]
    summernote_fields = ('body', 'excerpt')

    def has_delete_permission(self, request, obj=None):
        return False
