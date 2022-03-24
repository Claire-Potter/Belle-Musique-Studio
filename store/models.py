"""
Belle Musique Studio store app model configuration:

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
from django.db import models
# models is a callable within the django.db module of the Django project



class Category(models.Model):
    """
    Category model used to store all categories
    for music products
    """

    name = models.CharField(max_length=254)
    call_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """
        Definition of the plural name for admin
        """
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '%s' % (self.name)

    def get_call_name(self):
        """
        get call name utilised to return the category
        call name
        """
        return '%s' % (self.call_name)


class MusicProduct(models.Model):
    """
    Model used to store all music product
    items for the music store
    """
    category = (models.ForeignKey
                ('Category', null=True, blank=True, on_delete=models.SET_NULL))
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = (models.DecimalField
              (max_digits=6, decimal_places=2))
    rating = (models.DecimalField
              (max_digits=6, decimal_places=2, null=True, blank=True))
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_alt= models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.name)
