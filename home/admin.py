"""
Belle Musique Studio home app  adminconfiguration
"""
from django.contrib import admin

from .models import Contact, Cover, User,UserSubscription


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


class UserSubscriptionAdmin(admin.ModelAdmin):
    """.git/"""
    model = UserSubscription
    readonly_fields =('subscription_user_id', 'subscription_name', 'username', 'date')
    list_display = ('subscription_user_id', 'subscription_name', 'username', 'date')
    search_fields = ('subscription_user_id', 'subscription_name', 'date')

admin.site.register(UserSubscription, UserSubscriptionAdmin)


class UserAdmin(admin.ModelAdmin):
    """.git/"""
    model = User

admin.site.register(User, UserAdmin)
