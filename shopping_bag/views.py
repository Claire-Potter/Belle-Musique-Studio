"""
Belle Musique Studio checkout app views configuration

After correcting any pylint issues, I was still left with the issue
'class has no objects member', the object is only added when the screen
is  rendered in the browser, so the issue is not valid. I followed
the steps available for the following stack overflow:
https://stackoverflow.com/questions/45135263/class-has-no-objects-member
and created the .pylintrc file to customise the pylint settings to
prevent this error from displaying.

The view bag view renders the bag template through
the url. It is the current shopping bag, containing items
per the user's item selection.

The view lesson bag renders the lesson bag template through
the url. The lesson bag contains the lesson and subscription
selected by the user for purchase.

The add to bag view allows a user to add
a quantity of the specified product to the shopping bag.

The add lesson view allows a user to
add a lesson and subscription to the lesson bag.

The adjust bag view allows a user to
adjust the quantity of the specified
product to the specified amount.

The remove from bag view allows a user to
remove the item from the shopping bag.

The remove from lesson bag view allows a user to
remove the lesson and subscription from the lesson bag.

Messages definition from:
https://docs.djangoproject.com/en/4.0/ref/contrib/messages/

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
from django.contrib import messages
# Quite commonly in web applications, you need to display a one-time notification
# message (also known as “flash message”) to the user after processing a form or
#  some other types of user input.

# For this, Django provides full support for cookie- and session-based messaging,
# for both anonymous and authenticated users. The messages framework allows you
# to temporarily store messages in one request and retrieve them for display in a
# subsequent request (usually the next one). Every message is tagged with a specific level
# that determines its priority (e.g., info, warning, or error).
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)
# HttpResponse (source code) provides an inbound HTTP request to a Django web
# application with a text response. This class is most frequently used
# as a return object from a Django view.
# get_object_or_404 is a callable within the django.shortcuts module of the Django project.
# redirect is a callable within the django.shortcuts module of the Django project.
# render is a callable within the django.shortcuts module of the Django project.
# reverse is a callable within the django.urls module of the Django project.
from home.models import Cover
# Model imported from home app models.py
from store.models import MusicProduct
# Model imported from store app models.py


def view_bag(request):
    """
    The view bag view renders the bag template through
    the url. It is the current shopping bag, containing items
    per the user's item selection.

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp

    Created as per the Code Institute 'Boutique Ado'
    project.
    """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='bag')
    context = {
        'covers': covers,
        'cover': cover
    }

    return render(request, 'bag.html', context)

def view_lesson_bag(request):
    """
    The view lesson bag renders the lesson bag template through
    the url. The lesson bag contains the lesson and subscription
    selected by the user for purchase.

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp
    """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')
    context = {
        'covers': covers,
        'cover': cover
    }

    return render(request, 'lesson_bag.html', context)


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp

    item_id: the unique number to identify an item.

    Created as per the Code Institute 'Boutique Ado'
    project.
    """

    product = get_object_or_404(MusicProduct, pk=item_id)
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
                messages.success(request, f'Updated size {size.upper()} {product.name}'
                                           f'quantity to {bag[item_id]["items_by_size"][size]}')
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


def add_lesson(request):
    """
    Add a lesson and subscription to the lesson bag

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp
    """
    price_only = float(request.POST.get('price_only'))
    price_id = request.POST.get('priceId')
    name = request.POST.get('name')
    price = request.POST.get('price')
    caption = request.POST.get('caption')
    url = request.POST.get('url')
    dj_stripe_id = request.POST.get('dj_stripe')
    redirect_lesson_url = request.POST.get('redirect_lesson_url')
    lesson_bag = request.session.get('lesson_bag', {})
    lesson_bag[dj_stripe_id] = price_only, price_id, name, price, url, caption, dj_stripe_id
    messages.success(request, f'Added {name} to your bag')
    request.session['lesson_bag'] = lesson_bag
    return redirect(redirect_lesson_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified
    product to the specified amount.

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp

    item_id: the unique number to identify an item.

    Created as per the Code Institute 'Boutique Ado'
    project.
    """

    product = get_object_or_404(MusicProduct, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name}'
                                      f'quantity to {bag[item_id]["items_by_size"][size]}')
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


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp

    item_id: the unique number to identify an item.

    Created as per the Code Institute 'Boutique Ado'
    project.
    """

    try:
        product = get_object_or_404(MusicProduct, pk=item_id)
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


def remove_lesson_from_bag(request):
    """
    The remove from lesson bag view allows a user to
    remove the lesson and subscription from the lesson bag.

    request: The requests module allows you to send HTTP
    requests using Python.
    The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).

    Definition from https://www.w3schools.com/python/module_requests.asp
    """
    lesson_bag = request.session.get('lesson_bag', {})
    for dj_stripe_id, lesson_data in lesson_bag.items():

        lesson_bag_items = []
        name = lesson_data[2]
        lesson_bag_items.append({
                'name': name,
            })

    try:
        lesson_bag.pop(dj_stripe_id)
        messages.success(request, f'Removed {name} from your bag')

        request.session['lesson_bag'] = lesson_bag
        return HttpResponse(status=200)

    except Exception as e_m:
        messages.error(request, f'Error removing item: {e_m}')
        return HttpResponse(status=500)
