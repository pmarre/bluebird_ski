from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from services.models import Service


# Create your views here.


def view_cart(request):
    ''' view to return cart page '''
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified service to the shopping cart """
    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    size = None

    if 'boot_size' in request.POST:
        boot_size = request.POST['boot_size']
        ski_size = request.POST['ski_size']
        size = '{},{}'.format(boot_size, ski_size)

    if size:
        if item_id in list(cart.keys()):
            print(cart[item_id]['items_by_size'])
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Successfully updated {service.name}, boot size {boot_size}, ski size {ski_size}cm quantity to {cart[item_id]["items_by_size"][size]}!')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Successfully added {service.name}, boot size {boot_size}, ski size {ski_size}cm to cart!')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Successfully added {service.name}, boot size {boot_size}, ski size {ski_size}cm to cart!')

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Successfully updated {service.name} quantity to {cart[item_id]}!')
        else:
            cart[item_id] = quantity
            messages.success(
                request, f'Successfully added {service.name} to cart!')

    print(cart)
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust quantity of the specified service to the shopping cart """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    size = None

    if 'service_size' in request.POST:
        size = request.POST['service_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Successfully updated {service.name} quantity to {cart[item_id]["items_by_size"][size]}!')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(
                    request, f'Successfully removed {service.name} to cart!')

    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Successfully updated {service.name} quantity to {cart[item_id]}!')
        else:
            cart.pop(item_id)
            messages.success(
                request, f'Successfully removed {service.name} to cart!')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove specified service to the shopping cart """

    try:
        service = get_object_or_404(Service, pk=item_id)
        size = None
        if 'size' in request.POST:
            size = request.POST['size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request, f'Successfully removed {service.name} to cart!')

        else:
            cart.pop(item_id)
            messages.success(
                request, f'Successfully removed {service.name} to cart!')
        request.session['cart'] = cart

        return redirect(reverse('view_cart'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
