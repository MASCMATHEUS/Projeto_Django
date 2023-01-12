from django.urls import path

# pode se usar . em vez de from recipes import views
#  por que estão na mesma pasta
from . import views

urlpatterns = [
    path('', views.home),  # home = pagina inicial
    path('recipes/<int:id>/', views.recipe),

]
