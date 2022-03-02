""".git/"""
from django.db import models


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
