from django.shortcuts import render, get_object_or_404



def workshops(request):
    """ A view to show the music store """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='workshops')
    context = { 'covers': covers,
                'cover': cover}

    return render(request, 'workshops/workshops.html', context)
