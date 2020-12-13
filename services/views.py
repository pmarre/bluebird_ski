from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Service, Category
from .forms import ServiceForm
# Create your views here.


def all_services(request):
    ''' A view to show all services '''

    services = Service.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = [request.GET['category']]
            services = services.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'services': services,
        'current_categories': categories
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    ''' A detail view of service '''

    service = get_object_or_404(Service, pk=service_id)
    boot_sizes = []
    ski_sizes = []

    for i in range(120, 220, 10):
        ski_sizes.append(i)

    for i in range(15, 35, 1):
        boot_sizes.append(i)

    context = {
        'service': service,
        'boot_sizes': boot_sizes,
        'ski_sizes': ski_sizes,
    }

    return render(request, 'services/service_detail.html', context)


def add_service(request):
    """ Add a service to the store """
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(
                request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_service(request, service_id):
    """ Edit a service in the store """
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(
                request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


def delete_service(request, service_id):
    """ Delete a service from the store """
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')
    return redirect(reverse('services'))
