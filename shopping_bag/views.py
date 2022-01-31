from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from store.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag.html')
