from django.shortcuts import render

from utils.recipes.factory import make_recipe

# Create your views here.
# Cliente faz um HTTP request e recebe um HTTP response
# HTTP REQUEST

# render busca automaticamente a pasta template


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })
    ...
    # return HTTP response para Cliente


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })
