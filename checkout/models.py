"""
Belle Musique Studio checkout app model configuration:

The Order model is where a user's order details are created and stored.

The OrderLineItem model includes the product item details of
all products included in the order.

The SubscribedCustomer model is where a user's details are saved as a customer
record. This includes the customer details, user details and contact details.
details.

The SubscribedLineItem model is where a subscribed customer's subscription details
are saved as a subscription record. This includes the subscription details and
billing details.

SuperUser can access all models from the Site Admin page.
Admin provided necessary access only.

Definitions from https://www.fullstackpython.com
unless stated otherwise.

"""
import uuid
# UUIDField is a special field to store universally unique identifiers.
# https://www.geeksforgeeks.org/uuidfield-django-models

from django.conf import settings
# The Django settings file contains all of the configuration for a web application.
from django.db import models
# models is a callable within the django.db module of the Django project
from django.db.models import Sum
# One of the ways that aggregate values can be generated and returned using Django queries.
from django_countries.fields import CountryField
# A Django application that provides country choices for use with forms,
# flag icons static files, and a country field for models.
# https://pypi.org/project/django-countries/#:~:text=A%20Django%20application%20that%20provides,Installation
from djstripe.models import Customer, Subscription, Invoice
# Models are imported from models.py
from profiles.models import UserProfile
# Models are imported from profile app models.py
from store.models import MusicProduct
# Models are imported from store app models.py

class Order(models.Model):
    """
    The Order model is where a user's order details are created and stored.
    This includes the order_number, user details, shipping address and order
    details.
    It was created according to the Code Institute 'Boutique Ado' project.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = (self.lineitems.aggregate
                            (Sum('lineitem_total'))['lineitem_total__sum'] or 0)
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the order_number
        """
        return self.order_number


class OrderLineItem(models.Model):
    """
    The OrderLineItem model includes the product item details of
    all products included in the order.
    It was created according to the Code Institute 'Boutique Ado' project.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(MusicProduct, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the SKU on the order_number as a string
        """
        return f'SKU {self.product.sku} on order {self.order.order_number}'


class SubscribedCustomer(models.Model):
    """
    The SubscribedCustomer model is where a user's details are saved as a customer
    record. This includes the customer details, user details and contact details.
    details.
    The djstripe customer id from the Customer model is copied and
    saved as the subscribed_customer_id and the customer field has a one to one relationship
    with the djstripe Customer model.
    """

    subscribed_customer_id = models.CharField(max_length=250, null=True,
                                              blank=True, )
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=False,
                                    blank=False, )
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,
                                        null=False, blank=False,
                                        related_name='subscribed_customers')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """
        Returns the subscribed_customer_id as a string
        """
        return f'{self.subscribed_customer_id}'


class SubscriptionLineItem(models.Model):
    """
    The SubscribedLineItem model is where a subscribed customer's subscription details
    are saved as a subscription record. This includes the subscription details and
    billing details.
    The djstripe subscription id from the Subscription model is copied and
    saved as the subscribed_id and the subscription field has a Foreign Key relationship
    with the djstripe Subscription model. The customer field is has a Foreign Key relationship
    with the SubscribedCustomer model, linking all subscriptions back to the customer.
    """
    subscribed_id = models.CharField(max_length=250, null=True, blank=True, )
    subscription = models.ForeignKey(Subscription, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='subscription_lineitems',
                              )
    subscription_name = models.CharField(max_length=350, null=True, blank=True, )
    status =  models.CharField(max_length=250, null=True, blank=True, )
    customer= models.ForeignKey(SubscribedCustomer, blank=True,
                                on_delete=models.CASCADE, related_name='subscription_customer',
                                )
    quantity = models.IntegerField(null=True, blank=True, default=0)
    student = models.CharField(max_length=250, null=True, blank=True, editable=True)
    start_date= models.CharField(max_length=250, null=True, blank=True, )
    end_date = models.CharField(max_length=250, null=True, blank=True, )
    price= models.DecimalField(max_digits=6, decimal_places=2,
                                         null=True, blank=True, )
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=True, blank=True, )
    latest_invoice = models.ForeignKey(Invoice, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='subscription_invoice',
                              )

    original_lesson_bag = models.TextField(null=True, blank=True, default='')


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the subscription total.
        """
        self.lineitem_total = self.price
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the subscription number for the customer as a string
        """
        return f'Subscription number {self.subscription} for {self.customer}'
