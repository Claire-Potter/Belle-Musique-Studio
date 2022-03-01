""".git/"""
from django.contrib import admin
from .models import Lesson, Type, Subscription, StripeCustomer, SubscribedUser


class LessonAdmin(admin.ModelAdmin):
    """.git/"""
    list_display = (
        'sku',
        'name',
        'type',
    )

    ordering = ('sku',)


class LessonTypeAdmin(admin.ModelAdmin):
    """.git/"""
    list_display = (
        'call_type',
        'type',
    )


class SubscriptionAdmin(admin.ModelAdmin):
    """.git/"""
    list_display = (
        'name',
    )


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Type, LessonTypeAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(StripeCustomer)
admin.site.register(SubscribedUser)
