from django.db import models
# from djmoney.models.fields import MoneyField


class Category(models.Model):

    name = models.CharField(max_length=254)
    call_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '%s' % (self.name)

    def get_call_name(self):
        return '%s' % (self.call_name)


class Product(models.Model):
    category = (models.ForeignKey
                ('Category', null=True, blank=True, on_delete=models.SET_NULL))
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = (models.DecimalField
              (max_digits=6, decimal_places=2))
    rating = (models.DecimalField
              (max_digits=6, decimal_places=2, null=True, blank=True))
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '%s' % (self.name)
