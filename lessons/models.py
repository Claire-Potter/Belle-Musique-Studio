""".git/"""
from django.db import models
from django.contrib.auth.models import User


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


class StripeCustomer(models.Model):
    """.git/"""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    """.git/"""
    name = models.CharField(max_length=254)
    class SubscriptionType(models.TextChoices):
        """
        xxx
        """
        ANNUALLY = 'Annually', ('Annually')
        MONTHLY = 'Monthly', ('Monthly')
        WEEKLY = 'Weekly', ('Weekly')
    subscription = models.CharField(max_length=15, choices=SubscriptionType.choices,
                                default=SubscriptionType.MONTHLY,)
    class Duration(models.TextChoices):
        """
        xxx
        """
        THIRTY_MINUTES = '30 minutes', ('30 minutes')
        FORTYFIVE_MINUTES = '45 minutes', ('45 minutes')
    time_duration = models.CharField(max_length=15, choices=Duration.choices,
                                default=Duration.THIRTY_MINUTES,)
    class Pricing(models.TextChoices):
        """
        xxx
        """
        TWENTY_FIVE = '£ 25.00', ('£ 25.00')
        THIRTY_SEVEN = '£ 37.50', ('£ 37.50')
        HUNDRED = '£ 100.00', ('£ 100.00')
        HUNDRED_FIFTY = '£ 150.00', ('£ 150.00')
        TWELVE_HUNDRED = '£ 1200.00', ('£ 1200.00')
        EIGHTEEN_HUNDRED = '£ 1800.00', ('£ 1800.00')

    price = models.CharField(max_length=15, choices=Pricing.choices,
                                default=Pricing.TWENTY_FIVE,)
    lesson = models.ManyToManyField(Lesson, related_name='lesson', blank=True)
