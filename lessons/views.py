""".git/"""
import djstripe.models
import djstripe.settings
import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from djstripe.models import Product
from djstripe.models import Plan


from home.models import Cover
from .forms import LessonProductForm


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
        form_data = {
            'name': request.POST['name'],
            'description': request.POST['description'],
            'statement_descriptor': request.POST['statement_descriptor'],
            'unit_label': request.POST['unit_label'],
            'url': request.POST['url'],
            'caption': request.POST['caption'],
        }

        form = LessonProductForm(form_data)
        if form.is_valid():
            stripe_data =stripe.Product.create(name=request.POST['name'],
                description=request.POST['description'],
                statement_descriptor=request.POST['statement_descriptor'],
                unit_label=request.POST['unit_label'],
            type='service', active='true',images=[request.POST['url']])
            try:
                djstripe_obj = djstripe.models.Product.sync_from_stripe_data(stripe_data)
            except djstripe_obj.DoesNotExist:
                messages.error(request, (
                    "The lesson was not successfully created. Please contact an administrator"))
                add_form.delete()
            product = Product.objects.filter(name=request.POST['name']).latest('name')    
            form = LessonProductForm(form_data, instance=product)    
            add_form = form.save(commit=False)
            add_form.save()
            messages.success(request, 'Successfully added new lesson!')
            return redirect(reverse('lessons'))
        else:
            messages.error(request,
                           ('Failed to add new lesson. '
                            'Please ensure the form is valid.'))
    else:
        form = LessonProductForm()
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='product_manage')
    template = 'lessons/add_lesson.html'
    context = {
        'form': form,
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
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        form_data = {
            'name': request.POST['name'],
            'description': request.POST['description'],
            'statement_descriptor': request.POST['statement_descriptor'],
            'unit_label': request.POST['unit_label'],
            'url': request.POST['url'],
            'caption': request.POST['caption'],
        }

        form = LessonProductForm(form_data, instance=product)
        if form.is_valid():
            edit_form = form.save(commit=False)
            stripe.Product.modify(lesson_id, name=request.POST['name'],
            description=request.POST['description'],
            statement_descriptor=request.POST['statement_descriptor'],
            unit_label=request.POST['unit_label'],)
            edit_form.save()
            messages.success(request, 'Successfully updated lesson!')
            return redirect(reverse('lessons'))

        else:
            messages.error(request,
                           ('Failed to update lesson. '
                            'Please ensure the form is valid.'))
    else:
        form = LessonProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='product_manage')
    template = 'lessons/edit_lesson.html'
    context = {
        'form': form,
        'product': product,
        'covers': covers,
        'cover': cover,
    }

    return render(request, template, context)
