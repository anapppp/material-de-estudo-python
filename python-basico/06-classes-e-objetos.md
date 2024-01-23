# Classes e Objetos

Classes em Python são estruturas que permitem organizar e estruturar código de uma maneira orientada a objetos.

## Definição de Classe
   - Usada para criar objetos que combinam dados e comportamentos relacionados.
   - Define uma estrutura para os objetos a serem criados.

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
```

## Objetos
   - Instâncias de uma classe.
   - Criados a partir da classe e possuem atributos específicos.

```python
meu_carro = Carro(marca="Toyota", modelo="Corolla")
```

## Atributos
   - Variáveis associadas a uma classe ou objeto.
   - Armazenam informações sobre o objeto.

```python
print(meu_carro.marca)  # Saída: Toyota
```

## Métodos
   - Funções definidas dentro de uma classe.
   - Executam operações relacionadas ao objeto.

```python
class Carro:
    def ligar(self):
        print("O carro está ligado.")

meu_carro = Carro()
meu_carro.ligar()  # Saída: O carro está ligado.
```

## Construtor (`__init__`)
   - Método especial chamado automaticamente quando um objeto é criado.
   - Inicializa os atributos do objeto.

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
```

## Herança
   - Permite criar uma nova classe baseada em uma classe existente.
   - A nova classe herda atributos e métodos da classe pai.

```python
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia
```

## Encapsulamento
   - Oculta os detalhes internos da implementação da classe.
   - Atributos e métodos podem ser públicos, protegidos ou privados.

```python
class Carro:
    def __init__(self, marca, modelo):
        self._marca = marca  # Atributo protegido
        self.__modelo = modelo  # Atributo privado
```
