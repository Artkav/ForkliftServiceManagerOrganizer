from django.shortcuts import render


def index(request):
    context = {
        'title': 'Index Page'
    }
    return render(request, template_name='organizer/index.html', context=context)


def add_task(request):
    context = {
        'title': 'Add task page'
    }
    return render(request, template_name='organizer/add_task.html', context=context)


def customer_list(request):
    context = {
        'title': 'customer list'
    }
    return render(
        request, template_name='organizer/customer_list.html', context=context)


def customer(request):
    context = {
        'title': 'customer'
    }
    return render(
        request, template_name='organizer/customer.html', context=context)