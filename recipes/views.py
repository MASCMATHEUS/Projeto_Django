from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Cliente faz um HTTP request e recebe um HTTP response
# HTTP REQUEST


def home(request):
    return HttpResponse('home')
    ...
    # return HTTP response para Cliente


def contato(resquest):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
