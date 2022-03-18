"""
Belle Musique Studio home app  adminconfiguration
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from embed_video.admin import AdminVideoMixin

from .models import Contact, Cover, User, UserSubscription, StudentShowcase


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    The Contact admin set up reads the Contact model and allows
    the admin user to read and delete contact requests. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('name', 'email', 'created_on')
    list_filter = ('created_on', 'name')
    search_fields = ('name', 'email')


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


@admin.register(StudentShowcase)
class StudentShowcaseAdmin(SummernoteModelAdmin, AdminVideoMixin, admin.ModelAdmin):
    """
    The Tool admin set up reads the Tool model and allows
    the admin user to create a new tool by adding the
    required fields. Admin can also edit and delete.
    Django summernote is included to allow the admin user
    to style the body field.
    Cloudinary storage is utilised to store the images.
    Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('date', 'name',)
    search_fields = ['date', 'name',]
    summernote_fields = ('body', 'excerpt')

    def has_delete_permission(self, request, obj=None):
        return False
