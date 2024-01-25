# Módulos
O módulo é um arquivo com variaveis e funções que podem ser importadas

```python
import meu_modulo   # arquivo meu_modulo.py

meu_modulo.imprimir_texto("Hello World")   #funcao definida dentro de meu_modulo.py
```

```python
from meu_modulo import *  # arquivo meu_modulo.py

imprimir_texto("Hello World")   #funcao definida dentro de meu_moulo.py
```

> `import *` não é  uma boa prática, pois importa tudo e pode gerar conflito

# Pacotes

Para instalar:

```command
pip install colorama
```

```command
pip install -r requirements.txt
```
> Encontre pacotes python em https://pypi.org/

# Escopo

> Escopo local .vs. Escopo global

Para chamar uma variavel global dentro de um escopo local (uma função)  use `global`:

```python
bebida = "coca-cola"
def funcao:
    bebida = "fanta"      # variavel local
    global bebida         # chama a variavel global cujo valor é "coca-cola"   
```