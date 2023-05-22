from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def about(request):
    return render(request, 'about.html', context={
        'info': 'You need to try all of the possibilities of Django!',
    })

