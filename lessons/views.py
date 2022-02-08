from django.shortcuts import render, get_object_or_404
from home.models import Cover



def lessons(request):
    """ A view to show the lessons page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')
    context = { 'covers': covers,
                'cover': cover}

    return render(request, 'lessons/lessons.html', context)
from django.shortcuts import render
