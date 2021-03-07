from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothin in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ISF0cI8HXgSN0sEfXaCn7u0HiEB3hvVqotPp2eL1yGiBfLX8J3R2PNd1E7CpgwPAm3c7yfCpgKgwckUeoZatXE000HQfOPIlG',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
