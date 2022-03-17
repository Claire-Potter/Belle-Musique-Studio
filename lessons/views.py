""".git/"""
import djstripe.models
import djstripe.settings
import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from djstripe.models import Product


from home.models import Cover
from .forms import (LessonProductForm, LessonPriceForm,
                    LessonProductAddForm, LessonPriceAddForm)


def lessons_details(request):
    """ A view to show the lessons page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')
    lessons = Product.objects.all()
    context = {'covers': covers,
                'cover': cover,
                'lessons': lessons,
              }

    return render(request, 'lessons/lessons.html', context)


@login_required
def add_lesson(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        form = LessonProductAddForm(request.POST, prefix='product')
        p1_form = LessonPriceAddForm(request.POST, prefix = 'price_one')
        p2_form = LessonPriceAddForm(request.POST, prefix = 'price_two')
        p3_form = LessonPriceAddForm(request.POST, prefix = 'price_three')

        if form.is_valid() and p1_form.is_valid() and p2_form.is_valid() and p3_form.is_valid():
            stripe_data = stripe.Product.create(name=request.POST['product-name'],
            description=request.POST['product-description'],
            statement_descriptor=request.POST['product-statement_descriptor'],
            unit_label=request.POST['product-unit_label'],
            images=[request.POST['product-url']],
            type='service',
            active='true')
            try:
                djstripe_obj = djstripe.models.Product.sync_from_stripe_data(stripe_data)
                try:
                    amount_one = request.POST['price_one-amount']
                    amount_two = request.POST['price_two-amount']
                    amount_three = request.POST['price_three-amount']


                    def pound_to_cent(amount, truncate=True):
                        new_amount = float(amount) * 100
                        if truncate:
                            return int(new_amount)


                    new_amount_one = pound_to_cent(amount_one)
                    new_amount_two = pound_to_cent(amount_two)
                    new_amount_three = pound_to_cent(amount_three)


                    price_one_data = stripe.Plan.create(amount=new_amount_one,
                    currency=request.POST['price_one-currency'],
                    interval=request.POST['price_one-interval'],
                    nickname=request.POST['price_one-nickname'],
                    usage_type=request.POST['price_one-usage_type'],
                    product=djstripe_obj.id, active='true')
                    price_two_data = stripe.Plan.create(amount=new_amount_two,
                    currency=request.POST['price_two-currency'],
                    interval=request.POST['price_two-interval'],
                    nickname=request.POST['price_two-nickname'],
                    usage_type=request.POST['price_two-usage_type'], product=djstripe_obj.id,
                    active='true')
                    price_three_data = stripe.Plan.create(amount=new_amount_three,
                    currency=request.POST['price_three-currency'],
                    interval=request.POST['price_three-interval'],
                    nickname=request.POST['price_three-nickname'],
                    usage_type=request.POST['price_three-usage_type'], product=djstripe_obj.id,
                    active='true')
                    try:
                        price_one_stripe = (djstripe.models.
                                            Plan.sync_from_stripe_data(price_one_data))
                        price_two_stripe = (djstripe.models.
                                            Plan.sync_from_stripe_data(price_two_data))
                        price_three_stripe = (djstripe.models.
                                              Plan.sync_from_stripe_data(price_three_data))
                    except price_one_stripe.DoesNotExist:
                        messages.error(request, (
                        "The lesson was not successfully created. Please contact an administrator"))
                except djstripe_obj.DoesNotExist:
                    messages.error(request, (
                    "The lesson was not successfully created. Please contact an administrator"))
            except djstripe_obj.DoesNotExist:
                messages.error(request, (
                "The lesson was not successfully created. Please contact an administrator"))
            product = djstripe_obj.id
            price_1 = price_one_stripe.id
            price_2 = price_two_stripe.id
            price_3 = price_three_stripe.id
            form = LessonProductForm(request.POST, prefix='product')
            form.id = product
            p1_form.id = price_1
            p2_form.id = price_2
            p3_form.id = price_3
            add_form = form.save(commit=False)
            p1_form.cleaned_data['product'] = add_form
            p2_form.cleaned_data['product'] = add_form
            p3_form.cleaned_data['product'] = add_form
            price1 = p1_form.save(commit=False)
            price2 = p2_form.save(commit=False)
            price3 = p3_form.save(commit=False)
            add_form.save()
            price1.save()
            price2.save()
            price3.save()
            messages.success(request, 'Successfully added new lesson!')
            return redirect(reverse('lessons'))
        else:
            messages.error(request,
                           ('Failed to add new lesson. '
                            'Please ensure the form is valid.'))
    else:
        form = LessonProductAddForm(prefix='product')
        p1_form = LessonPriceAddForm(prefix = 'price_one')
        p2_form = LessonPriceAddForm(prefix = 'price_two')
        p3_form = LessonPriceAddForm(prefix = 'price_three')
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='product_manage')
    template = 'lessons/add_lesson.html'
    context = {
        'form': form,
        'p1_form': p1_form,
        'p2_form': p2_form,
        'p3_form': p3_form,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context)


@login_required
def edit_lesson(request, lesson_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=lesson_id)
    price_one = product.plan_set.order_by('id')[0]
    price_two = product.plan_set.order_by('id')[1]
    price_three = product.plan_set.order_by('id')[2]
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        form = LessonProductForm(request.POST, instance=product, prefix='product')
        p1_form = LessonPriceForm(request.POST, instance=price_one, prefix = 'price_one')
        p2_form = LessonPriceForm(request.POST, instance=price_two, prefix = 'price_two')
        p3_form = LessonPriceForm(request.POST, instance=price_three, prefix = 'price_three')
        if form.is_valid() and p1_form.is_valid() and p2_form.is_valid() and p3_form.is_valid():
            edit_form = form.save(commit=False)
            p1_form.cleaned_data['product'] = edit_form
            p2_form.cleaned_data['product'] = edit_form
            p3_form.cleaned_data['product'] = edit_form
            price1 = p1_form.save(commit=False)
            price2 = p2_form.save(commit=False)
            price3 = p3_form.save(commit=False)
            stripe_data = stripe.Product.modify(lesson_id, name=request.POST['product-name'],
            description=request.POST['product-description'],
            statement_descriptor=request.POST['product-statement_descriptor'],
            unit_label=request.POST['product-unit_label'],
            images=[request.POST['product-url']],)
            price_one_data = stripe.Plan.modify(price_one.id,
            nickname=request.POST['price_one-nickname'],)
            price_two_data = stripe.Plan.modify(price_two.id,
            nickname=request.POST['price_two-nickname'],)
            price_three_data = stripe.Plan.modify(price_three.id,
            nickname=request.POST['price_three-nickname'],)
            try:
                djstripe_obj = djstripe.models.Product.sync_from_stripe_data(stripe_data)
                djstripe.models.Plan.sync_from_stripe_data(price_one_data)
                djstripe.models.Plan.sync_from_stripe_data(price_two_data)
                djstripe.models.Plan.sync_from_stripe_data(price_three_data)

            except djstripe_obj.DoesNotExist:
                messages.error(request, (
                    "The lesson was not successfully edited. Please contact an administrator"))
            edit_form.save()
            price1.save()
            price2.save()
            price3.save()
            messages.success(request, 'Successfully updated lesson!')
            return redirect(reverse('lessons'))

        else:
            messages.error(request,
                            ('Failed to update lesson. '
                            'Please ensure the form is valid.'))
    else:
        form = LessonProductForm(instance=product,  prefix='product')
        p1_form = LessonPriceForm(instance=price_one, prefix = 'price_one')
        p2_form = LessonPriceForm(instance=price_two, prefix = 'price_two')
        p3_form = LessonPriceForm(instance=price_three, prefix = 'price_three')
        messages.info(request, f'You are editing {product.name}')
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='product_manage')
    template = 'lessons/edit_lesson.html'
    context = {
        'form': form,
        'p1_form': p1_form,
        'p2_form': p2_form,
        'p3_form': p3_form,
        'product': product,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context,)
