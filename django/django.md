# Django

![alt text](django.png)

> Framework = caixa de ferramentas

- Templates para montar páginas
- ORM para interagir com BD
- Forms
- Authorization
- Admin

## Inicializando um novo projeto em Django

> *Porque usar um ambiente virtual?* Para garantir que todos os pacotes sejam instalados localmente

1. Instalando o ambiente virtual
```
pip install virtualenv
```

2. Criando ambiente virtual (cria um diretorio chamado cadastro_curso_womakers)

``` 
python -m venv cadastro_curso_womakers
```


3. Ativando o ambiente virtual
```
 .\cadastro_curso_womakers\Scripts\activate
 ```

 4. Instalando o Django
 ```
 pip install django
 ```

 5. Criando um projeto Django
 ```
 django-admin startproject projeto_womakers .
 ```
 
 6. Iniciando um novo aplicativo
 ```
 python .\manage.py startapp base
 ```
 > Configurações gerais, como quais as rotas vamos usar, ficam no `manage.py`
>> Os principais arquivos que vamos usar são os `settings.py` e `url.py`

 > Coisas mais especificas, vão ficar no aplicativo `\base` que criamos (cadastro de usuários, cadastro de cursos, etc.)

7. Registrar o app instalado no `settings.py` do projeto, em `INSTALLED_APPS` 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base'
]
```
 8. Testando o servidor
 ```
 python .\manage.py runserver
 ```

## Views

Cada página do sistema é uma view. Para cada uma, criamos uma função.

1. Abrir `.\base\views.py`

2. Criar as Visualizações

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse('Hello World!')

def cadastro(request):
    pass
```

3. No arquivo `urls.py` incluir a URL

```python
from base.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio)
]
```

Podemos inserir uma estrutura HTML nessa view:

```python
def inicio(request):
    html='''
    <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Minha primeira página Django</title>
     </head>
     <body>
         <h1>Olá mundão de Deus!</h1>
     </body>
     </html>
    '''
    return HttpResponse(html)
```

Porém, o melhor e mais organizado é usar templates

## Usando Templates

1. Criar uma pasta `.\base\templates` onde todo o HTML vai ser colocado

2. Criar um arquivo `index.html` dentro da pasta

3. Renderizar o arquivo html na view

```python
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')
```

## Aprimorando templates

Em Django, tudo o que for CSS e JS precisa estar em uma pasta `.\base\static`, por exemplo, o que voce baixar do Bootstrap

2. Instalando o Bootstrap

```
pip install django-bootstrap-v5
```

2. Registrar o Bootstrap em `settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    'bootstrap5'    
]
```

## Django Forms

- classe do formulario - representa todo o formulario, quais campos
- field - campo específico
- widget - forma cmomo vai ser representado em HTML

1. Criar um arquivo `.\base\forms.py` 
2. Importar o forms
```python
from django import forms
```
3. Criar classes python para cada formulário

```python
class CadastroForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField
    senha = forms.CharField(widget=forms.PasswordInput)
``` 

4.  Chamar o form na `view.py`

```python
def cadastro(request):
    sucesso = False
    if request.method == 'GET':
        form = CadastroForm()
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)
```

5. Renderizar o form no bootstrap, no arquivo `cadastro.html`

```html
{% extends "inicio.html" %}
{% load bootstrap5 %}
{% block principal %}

  <h1 class="text-body-emphasis">Cursos online</h1>
  {% if sucesso %}
    <p class="alert alert-success"> Cadastro realizado com sucesso</>
  {% endif %}
  <form action="" method="POST" id="form">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button type="submit" class="btn btn-primary btn-block">Finalizar cadastro</button>
  </form>
  
{% endblock %}
```

## ModelForm

Em Django, cada classe no arquivo `models.py` vai representar uma tabela no banco de dados

1. Definir o banco de dados no arquivo `settings.py`
Aqui, vamos usar o default

2. Criar seus models
```python
from django.db import models

# Create your models here.
class Cadastro (models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
```

3. Fazer migração do banco de dados
```
 python .\manage.py makemigrations
 python .\manage.py migrate
 ```
 > Sempre que fizer alterações no banco de dados você vai precisar fazer a migração

 4. Conectar o formulário com o banco de dados

 Alterar o arquivo ´views.py´

 ```python
 from django.shortcuts import render
from django.http import HttpResponse
from base.forms import CadastroForm
from base.models import Cadastro  # importa o banco

# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')

def cadastro(request):
    sucesso = False
    if request.method == 'GET':
        form = CadastroForm()
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            sucesso = True
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            Cadastro.objects.create(
                nome=nome, email=email, senha=senha)  # envia pro banco
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)
 ``` 


 ### Simplificando o código

 Podemos evitar repetições e informações redundantes

1. Limpar o `forms.py`

```python
from django import forms
from base.models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
        widgets = {'senha': forms.PasswordInput()}
```

2. Limpar o  `views.py`

```python
def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()  # aqui, tudo do formulario é salvo no banco de dados
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)
```

# Admin

O Django gera a parte do administrativo automaticamente

1. Criando um superusuario

```
python .\manage.py createsuperuser
```
2. Acessar a URL `admin\`

Já é criado por default na `url.py`. Adicionar usuario e senha

> Usuario: anap  senha: 123

3. Registrar os models que voce quer que o admin tenha acesso

```python
from django.contrib import admin
from base.models import Cadastro

# Register your models here.
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    pass
```

4. Alterando a model class Cadastro pra que apareça o nome do usuário e o verbose

```python
class Cadastro (models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} [{self.email}]'

    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contato'
        ordering = ['-data']
```
5. Criando filtros e busca

```python
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']
``` 
