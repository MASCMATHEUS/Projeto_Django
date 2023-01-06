from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Cliente faz um HTTP request e recebe um HTTP response
# HTTP REQUEST

# render busca automaticamente a pasta template


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Matheus Alexandre'
    })
    ...
    # return HTTP response para Cliente


def contato(resquest):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
