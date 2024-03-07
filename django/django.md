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