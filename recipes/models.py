# Importação de class Usuario pre pronta do Django
from django.contrib.auth.models import User
from django.db import models

# nessesario registrar os models em admin para funcionar

# Metodo magico __str__
# quando a class que ele está e chamada como string ele é ativado
# Nesse caso está sendo usado
# para retorna o nome armazenado na variavel name


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


# Criando models
class recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    # slug remove caractere invalidos e us - para-separar-as-palavras
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings_time = models.ImageField()
    servings_time_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    # auto_now para atualizar a data toda vez que o objeto for alterado
    # auto_now_add atualiza a data no momento da criação
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
