"""
Belle Musique Studio home app model Configuration

Home model created to render a view for the homepage.
It stores the home page image and title.

Contact model created to render the contact page
and to store all contact requests submitted by users.
Admin can access this via the admin pane.

"""
from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    """
    Model created to store homepage data.
    Utilised to store the home image and create
    the Home page view using the template index.html.
    """
    name = models.CharField(max_length=80)
    home_image = models.ImageField('image')
    created_on = models.DateTimeField(auto_now_add=True)
    deletable = models.BooleanField(default=False, editable=False)

    class Meta:
        """
        Meta created to order the Home Model according
        to the created on date.
        """
        ordering = ['-created_on']
        verbose_name_plural = "Home"

    def __str__(self):
        return '%s' % (self.name)


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
