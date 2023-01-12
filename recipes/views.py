from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Cliente faz um HTTP request e recebe um HTTP response
# HTTP REQUEST

# render busca automaticamente a pasta template


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Matheus Alexandre'
    })
    ...
    # return HTTP response para Cliente


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Matheus Alexandre'
    })
