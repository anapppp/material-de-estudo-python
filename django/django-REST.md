# Django REST

> Traduzindo REST para PT-BR: Transferência do estado representacional

1. Instalando
```
pip install djangorestframework
```

Se der problema
```
python -m pip install djangorestframework
```

2. (opcional)

No arquivo `urls.py`

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('cadastro/', cadastro),
    path('curso/', include('cursos.urls', namespace='cursos'))
    path('api-auth/', include('rest_framework.urls'))
]
```

No terminal 
```
python .\manage.py startapp rest_api
```


3. Registrando no arquivo `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    'bootstrap5',
    'cursos',
    'rest_framework', 
    'rest_api'   
]
```

## Serializer 

Recurso para que outros sistemas possam ver nossa API

1. Criar um arquivo `rest_api/serializers.py`

```python
from rest_framework.serializers import ModelSerializer
from cursos.models import Curso


class CursoModelSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

```

2. No `views.py`

```python
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cursos.models import Curso
from rest_api.serializers import CursoModelSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello {request.data.get("nome")}'})
    else:
        return Response({'hello': 'World API'})


class CursoModelViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoModelSerializer
```

3. No arquivo `urls.pr`

```python
from django.urls import path
from rest_api.views import hello_world
from rest_framework.routers import SimpleRouter
from rest_api.views import CursoModelViewSet

app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False)
router.register('curso', CursoModelViewSet)

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world API')
]

urlpatterns += router.urls
``` 