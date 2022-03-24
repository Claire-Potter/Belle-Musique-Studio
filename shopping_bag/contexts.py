"""
Belle Musique Studio contexts configuration

Completed as per Code Institute 'Boutique Ado' Project
and customised for site.

bag contents context - calculate and define the data for
the shopping bag as per user's item selection.

lesson bag contents context - Calculate and define t
he data for the lesson bag as per user's lesson
and subscription selection.

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
from decimal import Decimal
# The decimal module provides support for fast correctly-rounded decimal floating point arithmetic.
# https://docs.python.org/3/library/decimal.html

from django.conf import settings
# The Django settings file contains all of the configuration for a web application
from django.shortcuts import get_object_or_404
# get_object_or_404 is a callable within the django.shortcuts module of the Django project.

from djstripe.models import Product
# Model is imported from djstripe models.py
from store.models import MusicProduct
# Model is imported from store models.py


def bag_contents(request):
    """
    Calculate and define the data for the shopping bag
    as per user's item selection.
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(MusicProduct, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(MusicProduct, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context


def lesson_bag_contents(request):
    """
    Calculate and define the data for the lesson bag
    as per user's lesson and subscription selection.
    """

    lesson_bag_items = []
    less_total = 0
    lesson_count = 0
    quantity = 0
    price_only = 0
    price_id = 0
    name = ''
    price = ''
    url = ''
    caption = ''
    lesson_bag = request.session.get('lesson_bag', {})

    for dj_stripe_id, lesson_data in lesson_bag.items():
        if isinstance(lesson_data, int):
            lesson = get_object_or_404(Product, pk=dj_stripe_id)
            price_only = lesson_data[0]
            price_id = lesson_data[1]
            name = lesson_data[2]
            price = lesson_data[3]
            url = lesson_data[4]
            caption = lesson_data[5]
            less_total = price_only
            lesson_count += 1
            quantity = 1
            lesson_bag_items.append({
                'dj_stripe_id': dj_stripe_id,
                'lesson': lesson,
                'price_only': price_only,
                'priceId' : price_id,
                'name': name,
                'price': price,
                'url': url,
                'caption': caption,
                'quantity': quantity,
                'lesson_data': lesson_data,
                'lesson_count': lesson_count
            })
        else:
            lesson = get_object_or_404(Product, pk=dj_stripe_id)
            price_only = lesson_data[0]
            price_id = lesson_data[1]
            name = lesson_data[2]
            price = lesson_data[3]
            url = lesson_data[4]
            caption = lesson_data[5]
            less_total = price_only
            quantity = 1
            lesson_count += 1
            lesson_bag_items.append({
                    'dj_stripe_id': dj_stripe_id,
                    'price_only': price_only,
                    'priceId': price_id,
                    'name': name,
                    'price': price,
                    'url': url,
                    'caption': caption,
                    'lesson': lesson,
                    'quantity': quantity,
                    'lesson_count': lesson_count
                })

    lesson_total = less_total

    context = {
        'lesson_bag_items': lesson_bag_items,
        'less_total': less_total,
        'lesson_count': lesson_count,
        'lesson_total': lesson_total,
        'quantity': quantity,
        'price_only': price_only,
        'priceId': price_id,
        'name': name,
        'url': url,
        'caption': caption,
        'price': price,
    }

    return context
