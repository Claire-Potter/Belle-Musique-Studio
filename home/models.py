"""
Belle Musique Studio home app model Configuration

Home model created to render a view for the homepage.
It stores the home page image and title.

Contact model created to render the contact page
and to store all contact requests submitted by users.
Admin can access this via the admin pane.

"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from djstripe.models import Customer, Subscription


class User(AbstractUser):
    """.git/"""
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    subscription = models.ForeignKey(Subscription, null=True, blank=True,on_delete=models.SET_NULL)


class Contact(models.Model):
    """
    Model created to render the contact page
    and save the contact request data.
    """
    username = models.ForeignKey(
               User, on_delete=models.CASCADE, related_name='contact',
               default='1', blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    deletable = models.BooleanField(default=True, editable=False)

    class Meta:
        """
        Meta created to order the Contact Model according
        to the created on date.
        """
        ordering = ['-created_on']
        verbose_name_plural = "Contact Requests"

    def __str__(self):
        return f'Contact request {self.body} by {self.name}'


class Cover(models.Model):
    """
    Model created to render the cover input
    and save the cover name and quote to reflect.
    """
    name = models.CharField(max_length=80)
    quote = models.CharField(max_length=250)
    page = models.CharField(max_length=15, default='home')

    class Meta:
        """
        Meta created to order the Cover Model according
        to the page.
        """
        ordering = ['page']

    def __str__(self):
        return f'Cover details: {self.name} and {self.quote}'
