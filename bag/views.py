from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get ('redirect_url')
    bag = request.session.get('bag', {}) #get's session 'bag' or creates one if it doesn't exist yet

    # Creates a dictionary of the item and quantity - if updates if already existing, else creates item and quantity
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag #overwrites session variable with updated version
    return redirect(redirect_url)
