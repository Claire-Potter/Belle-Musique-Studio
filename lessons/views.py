""".git/"""
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from djstripe.models import Product


from home.models import Cover


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
