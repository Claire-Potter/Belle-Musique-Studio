"""
Belle Musique Studio templatetags bag tools configuration

Completed as per Code Institute 'Boutique Ado' Project

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
from django import template
# import the template library from django to register a new template tag

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculation for subtotal
    """
    return price * quantity
