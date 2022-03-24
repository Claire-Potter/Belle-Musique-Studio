"""
Belle Musique Studio checkout app admin configuration

Definitions from https://www.fullstackpython.com
unless stated otherwise
"""
from django.contrib import admin
# The Django admin is an automatically-generated user interface
# for Django models. The admin interface can be heavily customized

from .models import (Order, OrderLineItem, SubscribedCustomer,
SubscriptionLineItem)
# Models are imported from models.py

class OrderLineItemAdminInline(admin.TabularInline):
    """
    The OrderLineItem admin provides an inline tabular view
    of the store product item details within the order.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    The Order admin stores the order details for
    all orders placed through the music store. The
    OrderLineItem model is included as an inline table.
    """
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
    """
    The SubscriptionLineItem admin provides an inline tabular view
    of the subscription details for each subscription taken out
    by the Subscribed Customer.
    """
    model = SubscriptionLineItem

    fields = ('subscribed_id', 'subscription_name', 'subscription',
              'customer', 'lineitem_total',
              'original_lesson_bag', 'status', 'start_date', 'end_date',
              'student', 'latest_invoice', 'price')


class SubscribedCustomerAdmin(admin.ModelAdmin):
    """
    The SubscribedCustomer admin stores the subscription details for
    customers who have subscribed to lessons through the lessons app. The
    SubscriptionLineItem model is included as an inline table.
    """
    inlines = (SubscriptionLineItemAdminInline,)


    fields = ('subscribed_customer_id', 'customer', 'user_profile', 'full_name',
              'email', 'phone_number', )

    list_display = ('subscribed_customer_id', 'customer', 'full_name')

    ordering = ('-date',)

admin.site.register(SubscribedCustomer, SubscribedCustomerAdmin)
