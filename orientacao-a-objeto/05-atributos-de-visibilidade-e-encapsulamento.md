# Atributos de visibilidade e encapsulamento

> Em python, todos os métodos declarados em uma classe são **públicos**.


# Convenções

- Atributos e métodos iniciados com um underscore são protegidos, só podem ser acessados por usuários avançados

- Atributos e métodos iniciados com dois underscores são privados, não podem ser alteradas


```python
class Exemplo:
    def _exemploDeMetodoProtegido:
        variavel1 = 1

    def __exemploDeMetodoPrivado:
        variavel2 = 2
```

> O compilador *NÃO AVISA O ERRO* de se tentar mudar um atributo privado, nem dá warning caso se tente alterar atributo protegido.

# Propriedades e Atributos

## Atributo:

- Geralmente, um atributo refere-se a uma característica de um objeto ou classe em Python.
- Em Python, os atributos são geralmente acessados usando a notação de ponto (objeto.atributo).
- Pode ser uma variável associada a uma instância de classe ou à própria classe.

## Propriedade:

- Em alguns contextos, uma propriedade pode ser vista como um atributo especial que possui métodos especiais chamados de "getter" e "setter".
- Propriedades são usadas para controlar o acesso, a atribuição e a manipulação de valores associados a um atributo.
- A propriedade é definida usando o decorador `@property` para o getter e opcionalmente `@<atributo>.setter` para o setter.


```python
class Retangulo:
    def __init__(self, comprimento, largura):
        self._comprimento = comprimento  # Atributo privado
        self._largura = largura          # Atributo privado

    @property
    def area(self):
        return self._comprimento * self._largura

    @property
    def comprimento(self):
        return self._comprimento

    @comprimento.setter
    def comprimento(self, novo_comprimento):
        if novo_comprimento < 0:
            raise ValueError("O comprimento não pode ser negativo")
        self._comprimento = novo_comprimento

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, nova_largura):
        if nova_largura < 0:
            raise ValueError("A largura não pode ser negativa")
        self._largura = nova_largura

# Exemplo de uso
meu_retangulo = Retangulo(comprimento=4, largura=5)
print(meu_retangulo.area)       # Acessando a propriedade 'area'
print(meu_retangulo.comprimento) # Acessando a propriedade 'comprimento'
meu_retangulo.comprimento = 6    # Modificando a propriedade 'comprimento'

```

> O método `setter` serve para atribuir valor à uma prpriedade