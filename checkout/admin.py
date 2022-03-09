""".git/"""
from django.contrib import admin

from .models import Order, OrderLineItem, SubscribedCustomer, SubscriptionLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """.git/"""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """.git/"""
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)


class SubscriptionLineItemAdminInline(admin.TabularInline):
    """.git/"""
    model = SubscriptionLineItem
    readonly_fields = ('lineitem_total',)


class SubscribedCustomerAdmin(admin.ModelAdmin):
    """.git/"""
    inlines = (SubscriptionLineItemAdminInline,)

    readonly_fields = ('date', 'customer',
                       'original_lesson_bag',
                       )

    fields = ('customer', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county','original_lesson_bag',
              )

    list_display = ('customer', 'date', 'full_name')

    ordering = ('-date',)

admin.site.register(SubscribedCustomer, SubscribedCustomerAdmin)
