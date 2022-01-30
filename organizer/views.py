from django.shortcuts import render


def index(request):
    context = {
        'title': 'Index Page'
    }
    return render(request, template_name='organizer/index.html', context=context)
