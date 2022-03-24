"""
Belle Musique Studio store app views configuration

The music store view is a view to show the music store

All products is a view to show all  music products,
including sorting and search queries

Product detail is a view to show individual product details

Add product is a view to add a product to the store

Edit product is a view to edit a product

Delete product is a view to delete a product from the store

All views created as per the Code Institute's 'Boutique Ado'
project.

After correcting any pylint issues, I was still left with the issue
'class has no objects member', the object is only added when the screen
is  rendered in the browser, so the issue is not valid. I followed
the steps available for the following stack overflow:
https://stackoverflow.com/questions/45135263/class-has-no-objects-member
and created the .pylintrc file to customise the pylint settings to
prevent this error from displaying.

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
from django.contrib.auth.decorators import login_required
# @login_required: Django's login_required function is used to secure views
# in your web applications by forcing the client to
# authenticate with a valid logged-in User.
from django.db.models.functions import Lower
# Accepts a single text field or expression and returns the lowercase representation.
from django.shortcuts import get_object_or_404, redirect, render, reverse
# get_object_or_404 is a callable within the django.shortcuts module of the Django project.
# redirect is a callable within the django.shortcuts module of the Django project.
# render is a callable within the django.shortcuts module of the Django project.
# reverse is a callable within the django.urls module of the Django project.

from home.models import Cover
# Model is imported from home app models.py

from .forms import ProductForm
# Form imported from forms.py
from .models import Category, MusicProduct
# Models imported from models.py


def music_store(request):
    """
    A view to show the music store

    request: The requests module allows you to send HTTP
    requests using Python.
    """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='music_store')
    context = {'covers': covers,
                'cover': cover}

    return render(request, 'music_store.html', context)


def all_products(request):
    """
    A view to show all  music products,
    including sorting and search queries

    request: The requests module allows you to send HTTP
    requests using Python.
    """

    products = MusicProduct.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_sorting = f'{sort}_{direction}'
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='product')

    context = {
        'products': products,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'covers': covers,
        'cover': cover,
    }

    return render(request, 'products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details

    request: The requests module allows you to send HTTP
    requests using Python.

    product_id: the unique number used to identify a product.
    """

    product = get_object_or_404(MusicProduct, pk=product_id)
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='product_detail')
    context = {
        'product': product,
        'covers': covers,
        'cover': cover,
        'is_shopping_bag': True
    }

    return render(request, 'product_detail.html', context)



@login_required
def add_product(request):
    """
    Add a product to the store

    request: The requests module allows you to send HTTP
    requests using Python.
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='product_manage')
    template = 'add_product.html'
    context = {
        'form': form,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store

    request: The requests module allows you to send HTTP
    requests using Python.

    product_id: the unique number used to identify a product.
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(MusicProduct, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='product_manage')
    template = 'edit_product.html'
    context = {
        'form': form,
        'product': product,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store

    request: The requests module allows you to send HTTP
    requests using Python.

    product_id: the unique number used to identify a product.
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(MusicProduct, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
