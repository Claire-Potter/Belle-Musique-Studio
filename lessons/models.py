""".git/"""
from django.db import models
from djstripe.models import Customer, Subscription
from home.models import User
from profiles.models import UserProfile


class Type(models.Model):
    """.git/"""

    type = models.CharField(max_length=254)
    call_type = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """.git/"""
        verbose_name_plural = 'Lesson Types'


    def __str__(self):
        return '%s' % (self.type)

    def get_call_type(self):
        """.git/"""
        return '%s' % (self.call_type)


class Lesson(models.Model):
    """.git/"""
    type = (models.ForeignKey
                ('Type', null=True, blank=True, on_delete=models.SET_NULL))
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s' % (self.name)


class SubscribedCustomer(models.Model):
    """.git/"""

    username = models.OneToOneField(
               User, on_delete=models.CASCADE, related_name='subscription_user',
               default='1', blank=True)
    customer = models.OneToOneField(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    profile = models.OneToOneField(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return '%s' % (self.profile)


class SubscriptionLineItem(models.Model):
    """.git/"""
    subscription = models.ForeignKey(Subscription, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='subscription_lineitems')
    lesson = (models.ForeignKey
             ('Lesson', null=True, blank=True, on_delete=models.SET_NULL))
    customer= models.ForeignKey(SubscribedCustomer, blank=False,
                              on_delete=models.CASCADE, related_name='subscription_customer')
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the subscription total.
        """
        self.lineitem_total = self.subscription.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Subscription number {self.subscription} for {self.SubscribedCustomer.profile}'
