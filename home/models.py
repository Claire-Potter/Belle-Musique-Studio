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
from embed_video.fields import EmbedVideoField
from djstripe.models import Customer, Subscription


class User(AbstractUser):
    """.git/"""
    customer = models.OneToOneField(Customer, null=True, blank=True, on_delete=models.CASCADE)


class UserSubscription(models.Model):
    """.git/"""
    username = models.ForeignKey(User, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='userlineitems',
                              editable=False)
    subscription_user_id = models.CharField(max_length=350, unique=True, null=True, blank=True,
                                             editable=False)
    subscription_name = models.CharField(max_length=350, null=True, blank=True,
                                          editable=False)
    subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL,
                                     editable=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        """
        Meta created to order the Image Model according
        to the order_number. It also determines the latest
        entry saved to the model referring to the added date.
        """
        ordering = ['date']
        get_latest_by = ['date']


    def __str__(self):
        return f'{self.subscription}'


class Contact(models.Model):
    """
    Model created to render the contact page
    and save the contact request data.
    """
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

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


class StudentShowcase(models.Model):
    """
    Utilised to store the data and
    create the view using the step_tool.html template.
    """
    name = models.CharField(max_length=80, unique=True,
                             default='placeholder')
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video_name = models.CharField(max_length=100, blank=True,
                                  default='placeholder')
    video_url = EmbedVideoField(blank=True)
    date = models.DateTimeField(auto_now_add=True)



    class Meta:
        """
        Meta created to order the Tools Model according
        to order number assigned.
        """
        ordering = ['date']
        verbose_name_plural = "Student Showcase"

    # The string is set to return the Title field if it exists
    #  else a blank string
    def __str__(self):
        return '%s' % (self.name) if self.name else ' '
