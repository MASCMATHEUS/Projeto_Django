from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),  # home = pagina inicial
    path('sobre/', sobre),
    path('contato/', contato),

]
