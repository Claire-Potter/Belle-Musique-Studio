from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse

from home.models import Cover

from .forms import ProductForm
from .models import Category, MusicProduct


def music_store(request):
    """ A view to show the music store """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='music_store')
    context = {'covers': covers,
                'cover': cover}

    return render(request, 'music_store.html', context)


def all_products(request):
    """ A view to show all products, including sorting and search queries """

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
    """ A view to show individual product details """

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
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
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
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
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
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(MusicProduct, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
