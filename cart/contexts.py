from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):

    cart_items = []
    total = 0
    service_count = 0
    cart = request.session.get('cart', {})
    u_name = str(request.user)

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            service = get_object_or_404(Service, pk=item_id)
            total += item_data * service.price
            service_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'service': service,
            })
        else:
            service = get_object_or_404(Service, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * service.price
                service_count += quantity
                size = size.split(',')
                combined_size = '{},{}'.format(size[0], size[1])
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'service': service,
                    'size': combined_size,
                    'boot_size': size[0],
                    'ski_size': size[1],
                })

    if u_name == 'AnonymousUser':
        grand_total = total
        discount = 0
    else:
        discount = total * Decimal(0.1)
        grand_total = total - discount

    context = {
        'cart_items': cart_items,
        'total': total,
        'service_count': service_count,
        'grand_total': grand_total,
        'discount': discount,
        'total': total,

    }

    return context
