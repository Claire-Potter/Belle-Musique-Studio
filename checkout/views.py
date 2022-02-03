from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from home.models import Cover
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='checkout')
    template = 'checkout.html'
    context = {
        'covers': covers,
        'cover': cover,
        'order_form': order_form,
        'stripe_public_key': 'pk_test_0SMREd7Vdweb1MGRi8S0EycR00JVzSAs5O',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
