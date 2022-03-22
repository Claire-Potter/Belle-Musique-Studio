""" git """
from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404

from djstripe.models import Product
from store.models import MusicProduct


def bag_contents(request):
    """git"""

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
    """.git/"""

    lesson_bag_items = []
    less_total = 0
    lesson_count = 0
    quantity = 0
    price_only = 0
    priceId = 0
    name = ''
    price = ''
    url = ''
    caption = ''
    lesson_bag = request.session.get('lesson_bag', {})

    for dj_stripe_id, lesson_data in lesson_bag.items():
        if isinstance(lesson_data, int):
            lesson = get_object_or_404(Product, pk=dj_stripe_id)
            price_only = lesson_data[0]
            priceId = lesson_data[1]
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
                'priceId' : priceId,
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
            priceId = lesson_data[1]
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
                    'priceId': priceId,
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
        'priceId': priceId,
        'name': name,
        'url': url,
        'caption': caption,
        'price': price,
    }

    return context
