from django.contrib import messages
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)

from home.models import Cover
from lessons.models import Lesson
from store.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='bag')
    context = {
        'covers': covers,
        'cover': cover
    }

    return render(request, 'bag.html', context)

def view_lesson_bag(request):
    """ A view that renders the bag contents page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='bag')
    context = {
        'covers': covers,
        'cover': cover
    }

    return render(request, 'lesson_bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def add_lesson(request, lesson_id):
    """.git/"""
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    lesson_bag = request.session.get('lesson_bag', {})
    if lesson_id in list(lesson_bag.keys()):
        lesson_bag[lesson_id] += quantity
        messages.success(request, f'Updated {lesson.name} quantity to {lesson_bag[lesson_id]}')
    else:
        lesson_bag[lesson_id] = quantity
        messages.success(request, f'Added {lesson.name} to your lesson_bag')

    request.session['lesson_bag'] = lesson_bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def adjust_lesson_bag(request, lesson_id):
    """Adjust the quantity of the specified product to the specified amount"""

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    quantity = int(request.POST.get('quantity'))
    lesson_bag = request.session.get('lesson_bag', {})

    if quantity > 0:
        lesson_bag[lesson_id] = quantity
        messages.success(request, f'Updated {lesson.name} quantity to {lesson_bag[lesson_id]}')
    else:
        lesson_bag.pop(lesson_id)
        messages.success(request, f'Removed {lesson.name} from your lesson_bag')

    request.session['lesson_bag'] = lesson_bag
    return redirect(reverse('view_lesson_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e_m:
        messages.error(request, f'Error removing item: {e_m}')
        return HttpResponse(status=500)


def remove_lesson_from_bag(request, lesson_id):
    """Remove the item from the shopping bag"""

    try:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        lesson_bag = request.session.get('lesson_bag', {})
        lesson_bag.pop(lesson_id)
        messages.success(request, f'Removed {lesson.name} from your lesson_bag')

        request.session['lesson_bag'] = lesson_bag
        return HttpResponse(status=200)

    except Exception as e_m:
        messages.error(request, f'Error removing item: {e_m}')
        return HttpResponse(status=500)
