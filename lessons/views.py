"""
Belle Musique Studio lessons app views configuration

After correcting any pylint issues, I was still left with the issue
'class has no objects member', the object is only added when the screen
is  rendered in the browser, so the issue is not valid. I followed
the steps available for the following stack overflow:
https://stackoverflow.com/questions/45135263/class-has-no-objects-member
and created the .pylintrc file to customise the pylint settings to
prevent this error from displaying.

Lesson Details - A view to display the available lessons (djstripe products)
and the available subscription plan options per lesson
(djstripe plans). A user will select the lesson they wish to
subscribe to and add to their lesson bag.

Add Lesson view set up to enable a staff member to
add a djstripe product and three djstripe plans. It will be saved
to the Product model and the Plan model.

Edit Lesson view - set up to enable a staff member to
edit a djstripe product and three djstripe plans. It will be saved
to the Product model and the Plan model.

Messages definition from:
https://docs.djangoproject.com/en/4.0/ref/contrib/messages/

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
import djstripe.models
# Models are imported from djstripe models
# dj-stripe implements all of the Stripe models, for Django.
# https://pypi.org/project/dj-stripe/2.2.3/
import djstripe.settings
# Settings imported from djstripe
import stripe
# A Python library for Stripe’s API.
# https://pypi.org/project/stripe/
from django.conf import settings
# The Django settings file contains all of the configuration for a web application.
from django.shortcuts import get_object_or_404, redirect, render, reverse
# get_object_or_404 is a callable within the django.shortcuts module of the Django project.
# redirect is a callable within the django.shortcuts module of the Django project.
# render is a callable within the django.shortcuts module of the Django project.
# reverse is a callable within the django.urls module of the Django project.
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
from djstripe.models import Product
# Models are imported from djstripe models.py


from home.models import Cover
# Model imported from home app models.py
from .forms import (LessonProductForm, LessonPriceForm,
                    LessonProductAddForm, LessonPriceAddForm)
# Forms are imported from forms.py


def lessons_details(request):
    """
    A view to display the available lessons (djstripe products)
    and the available subscription plan options per lesson
    (djstripe plans). A user will select the lesson they wish to
    subscribe to and add to their lesson bag.

    Only one lesson can be processed per checkout so the select buttons
    are set up to be inactive when a lesson is in the lesson bag.

    request: The requests module allows you to send HTTP
    requests using Python.
    """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')
    lessons = Product.objects.all()
    context = {'covers': covers,
                'cover': cover,
                'lessons': lessons}

    return render(request, 'lessons/lessons.html', context)


@login_required
def add_lesson(request):
    """
    Add Lesson view set up to enable a staff member to
    add a djstripe product and three djstripe plans. It will be saved
    to the Product model and the Plan model.

    request: The requests module allows you to send HTTP
    requests using Python.

    Code written by me in alignment with code learnt through the
    'Boutique Ado' project and the Stripe API guide
    https://stripe.com/docs/api
    """
    # only staff can add a lesson
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    # if the forms have been submitted fetch the completed posted forms,
    # indicating a prefix for the id per form.
    # provide the stripe API key
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        form = LessonProductAddForm(request.POST, prefix='product')
        p1_form = LessonPriceAddForm(request.POST, prefix = 'price_one')
        p2_form = LessonPriceAddForm(request.POST, prefix = 'price_two')
        p3_form = LessonPriceAddForm(request.POST, prefix = 'price_three')

        # if all of the forms are validated create the product in stripe
        if form.is_valid() and p1_form.is_valid() and p2_form.is_valid() and p3_form.is_valid():
            stripe_data = stripe.Product.create(name=request.POST['product-name'],
             description=request.POST['product-description'],
             statement_descriptor=request.POST['product-statement_descriptor'],
             unit_label=request.POST['product-unit_label'],
             images=[request.POST['product-url']],
             type='service',
             active='true')
            try:
                # sync the data from stripe product through djstripe
                djstripe_obj = djstripe.models.Product.sync_from_stripe_data(stripe_data)
                product = djstripe_obj
                new_form = LessonProductAddForm(request.POST, prefix='product', instance=product)
                try:
                    # the original format of the amount is in pounds, it needs to be converted
                    # in to cents to be created on stripe
                    # code added by me.
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

                    # once the amounts have been converted the three prices
                    # are created on stripe
                    price_one_price = (stripe
                                       .Plan.create(amount=new_amount_one,
                                                    currency=request.POST['price_one-currency'],
                                                    interval='week',
                                                    nickname=request.POST['price_one-nickname'],
                                                    product=djstripe_obj.id, active='true',
                                                    usage_type=request.POST['price_one-usage_type']))
                    price_two_price = (stripe
                                       .Plan.create(amount=new_amount_two,
                                                    currency=request.POST['price_two-currency'],
                                                    interval='month',
                                                    product=djstripe_obj.id, active='true',
                                                    nickname=request.POST['price_two-nickname'],
                                                    usage_type=request.POST['price_two-usage_type']))
                    price_three_price = (stripe
                                         .Plan.create(amount=new_amount_three,
                                                      currency=request.POST['price_three-currency'],
                                                      interval='year',
                                                      product=djstripe_obj.id, active='true',
                                                      nickname=request.POST['price_three-nickname'],
                                                      usage_type=request.POST['price_three-usage_type'],
                                                      trial_period_days=7))
                    try:
                        # sync the data from the Plan model through djstripe
                        djstripe.models.Plan.sync_from_stripe_data(price_one_price)
                        djstripe.models.Plan.sync_from_stripe_data(price_two_price)
                        djstripe.models.Plan.sync_from_stripe_data(price_three_price)
                    # error message if the new product synced from djstripe doesn't exist
                    except djstripe_obj.DoesNotExist:
                        messages.error(request, ('The lesson was not '
                                                 'successfully created. '
                                                 'Please contact an administrator'))
                except djstripe_obj.DoesNotExist:
                    messages.error(request, ('The lesson was not successfully '
                                             'created. '
                                             'Please contact an administrator'))
            except djstripe_obj.DoesNotExist:
                messages.error(request, ('The lesson was not successfully created. '
                                         'Please contact an administrator'))
            # save the product
            add_form = new_form.save(commit=False)
            add_form.save()
            messages.success(request, 'Successfully added new lesson!')
            # return to the lessons page
            return redirect(reverse('lessons'))
        # error message if the forms cannot be validated
        else:
            messages.error(request,
                           ('Failed to add new lesson. '
                            'Please ensure the form is valid.'))
    else:
        # initial forms data before the forms have been created. Default values are
        # added for week, month, year and trial periods, as all products align in terms
        # of the subscriptions provided and the annual subscription includes a 7 day trial
        # i.e. 1 free weekly lesson. The fields are read only
        form = LessonProductAddForm(prefix='product')
        p1_form = LessonPriceAddForm(prefix = 'price_one', initial={'interval': 'week',
                                                'trial_period_days': 0})
        p2_form = LessonPriceAddForm(prefix = 'price_two',  initial={'interval': 'month',
                                                'trial_period_days': 0})
        p3_form = LessonPriceAddForm(prefix = 'price_three',  initial={'interval': 'year',
                                                'trial_period_days': 7})
    # fetch the page data
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
    """
    Edit Lesson view - set up to enable a staff member to
    edit a djstripe product and three djstripe plans. It will be saved
    to the Product model and the Plan model.

    request: The requests module allows you to send HTTP
    requests using Python.
    lesson_id: the number which uniquely identifies the
    lesson (djstripe product)

    Code written by me in alignment with code learnt through the
    'Boutique Ado' project and the Stripe API guide
    https://stripe.com/docs/api
    """
    # only staff can edit a lesson
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))
    # fetch the selected product and plans to be edited
    product = get_object_or_404(Product, id=lesson_id)
    price_one = product.plan_set.order_by('id')[0]
    price_two = product.plan_set.order_by('id')[1]
    price_three = product.plan_set.order_by('id')[2]
    # if the forms have been submitted fetch the completed posted forms,
    # and set the instance to the product and plans being edited
    # indicating a prefix for the id per form.
    # provide the stripe API key
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        form = LessonProductForm(request.POST, instance=product, prefix='product')
        p1_form = LessonPriceForm(request.POST, instance=price_one, prefix = 'price_one')
        p2_form = LessonPriceForm(request.POST, instance=price_two, prefix = 'price_two')
        p3_form = LessonPriceForm(request.POST, instance=price_three, prefix = 'price_three')
        # if all of the forms are validated edit the product and plans in stripe
        if form.is_valid() and p1_form.is_valid() and p2_form.is_valid() and p3_form.is_valid():
            edit_form = form.save(commit=False)
            p1_form.cleaned_data['product'] = edit_form
            p2_form.cleaned_data['product'] = edit_form
            p3_form.cleaned_data['product'] = edit_form
            price1 = p1_form.save(commit=False)
            price2 = p2_form.save(commit=False)
            price3 = p3_form.save(commit=False)
            stripe_data = (stripe.
                           Product.
                           modify(lesson_id, name=request.POST['product-name'],
                                  description=request.POST['product-description'],
                                  statement_descriptor=request.POST['product-statement_descriptor'],
                                  unit_label=request.POST['product-unit_label'],
                                  images=[request.POST['product-url']],))
            price_one_data = (stripe.
                              Plan.
                              modify(price_one.id,
                                     nickname=request.POST['price_one-nickname'],))
            price_two_data = (stripe.
                              Plan
                              .modify(price_two.id,
                                      nickname=request.POST['price_two-nickname'],))
            price_three_data = (stripe.
                                Plan.
                                modify(price_three.id,
                                       nickname=request.POST['price_three-nickname'],))
            try:
                # sync the data with the product and plan models through djstripe
                djstripe_obj = djstripe.models.Product.sync_from_stripe_data(stripe_data)
                djstripe.models.Plan.sync_from_stripe_data(price_one_data)
                djstripe.models.Plan.sync_from_stripe_data(price_two_data)
                djstripe.models.Plan.sync_from_stripe_data(price_three_data)
            # error message if the product synced from djstripe can't be found
            except djstripe_obj.DoesNotExist:
                messages.error(request, (
                    'The lesson was not successfully edited. Please contact an administrator'))
            # save the edited product and plans
            edit_form.save()
            price1.save()
            price2.save()
            price3.save()
            messages.success(request, 'Successfully updated lesson!')
            # return to the lessons page
            return redirect(reverse('lessons'))
        # error message if the forms cannot be validated
        else:
            messages.error(request,
                            ('Failed to update lesson. '
                            'Please ensure the form is valid.'))
    else:
        # initial forms data before the forms have been created.
        form = LessonProductForm(instance=product,  prefix='product')
        p1_form = LessonPriceForm(instance=price_one, prefix = 'price_one')
        p2_form = LessonPriceForm(instance=price_two, prefix = 'price_two')
        p3_form = LessonPriceForm(instance=price_three, prefix = 'price_three')
        messages.info(request, f'You are editing {product.name}')
    # fetch the page data
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
