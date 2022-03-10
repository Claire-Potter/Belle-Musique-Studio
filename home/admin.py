"""
Belle Musique Studio home app  adminconfiguration
"""
from django.contrib import admin

from .models import Contact, Cover, User,UserLineItem


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    The Contact admin set up reads the Contact model and allows
    the admin user to read and delete contact requests. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('name', 'email', 'created_on',
                    'deletable')
    list_filter = ('created_on', 'name', 'deletable')
    search_fields = ('name', 'email', 'deletable')


@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):
    """
    The Cover admin set up reads the Cover model and allows
    the admin user to read and delete input for the cover name and cover quotes
    used across the site.
    """
    list_display = ('name', 'quote', 'page')
    list_filter = ('name', 'quote', 'page')
    search_fields = ('name', 'quote', 'page')


class UserLineItemAdminInline(admin.TabularInline):
    """.git/"""
    model = UserLineItem
    fields = ('subscription_user_id', 'subscription_name')


class UserAdmin(admin.ModelAdmin):
    """.git/"""
    inlines = (UserLineItemAdminInline,)

admin.site.register(User, UserAdmin)
