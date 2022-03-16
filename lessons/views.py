""".git/"""
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from djstripe.models import Product


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
        form = LessonProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added new lesson and subscription!')
            return redirect(reverse('lessons'))
        else:
            messages.error(request,
                           ('Failed to add new lesson and subscription. '
                            'Please ensure the form is valid.'))
    else:
        form = LessonProductForm()
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='product_management')
    template = 'add_lesson.html'
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
        form = LessonProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
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
