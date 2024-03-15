# Testes com Pytest-Django

1. Instalar pytest-django, pytest e model_bakery

```
pip install pytest-django
pip install pytest
pip install model_bakery
```

2. Criar um arquivo chamado `pytest.ini` no diretório principal

```python
[pytest]
DJANGO_SETTINGS_MODULE =projeto_womakers.settings
python_files = tests.py test_*.py *_test.py
```

3. Apagar o arquivo `test.py` do diretório do aplicativo que você quer testar, e criar um diretório e um arquivo `tests/__init__.py`

4. Criar `tests/test_models.py` para testar as models

```python
from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest

@pytest.mark.django_db
def test_str_deve_retornar_string_formatada():
    curso = baker.make(
        Curso,
        titulo='Java',
        data_do_curso = date.today(),
        carga_horaria = '40'
    )
    assert str(curso) == 'Java: 2024-03-15 - 40'
```

5. Usando fixture

```python
from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest

@pytest.fixture
def curso():
    curso = baker.make(
        Curso,
        titulo='Java',
        data_do_curso = date.today(),
        carga_horaria = '40'
    )
    return curso
    
    
@pytest.mark.django_db
def test_str_deve_retornar_string(curso):
    assert str(curso) == 'Java: 2024-03-15 - 40'
```

6. Criar `tests/test_views.py` para testar as views

```python
from pytest_django.asserts import assertTemplateUsed
import pytest

@pytest.mark.django_db
def test_curso_view_deve_retornar_template(client):
    response = client.get('/curso/criar_curso')
    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_curso.html')
    
```