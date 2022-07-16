from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Valney Filho'
    })


def contact(request):
    return render(request, 'recipes/contato.html')
