# Construtores e Destrutores

**Construtores** são métodos especiais, e são chamados durante a instanciação de um objeto. Se não for explicitamente declarado, ele é declarado implicitamente.

```python

class ExemploDeClasse:
    def __init__(self, nome):
        self.nome = nome

    def __del__(self, nome):
        self.nome = nome
```

**Destrutores** são métodos chamados para destruir objetos e livrar espaço na memória. É possível destruir um objeto antes do encerramento da execução do programa usando a palavra reservada `del`.


```python
Classe1 = ExemploDeClasse("Classe 1")
del Classe1
```

