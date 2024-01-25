# Programação Orientada a Objetos

- É um paradigma
- Objetos reune propriedades e comportamentos desse sujeito
- Objetos sao auocontidos e reutilizáveis
- Conceitos:
  - classes
  - herança
  - encapsulamento
  - abstrações
  - polimorfismo

# Classes


  ```python
  class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, aumento):
        self.velocidade += aumento
        print(f'O carro está agora a {self.velocidade} km/h.')

    def frear(self, reducao):
        self.velocidade -= reducao
        print(f'O carro está agora a {self.velocidade} km/h.')

    def obter_informacoes(self):
        return f'Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Velocidade: {self.velocidade} km/h'
        
    def __str__(self):
        return f'Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Velocidade: {self.velocidade} km/h'


  # Exemplo de uso da classe Carro
  meu_carro = Carro(modelo='Sedan', ano=2022, cor='Azul')
  carro_do_vizinho = Carro(modelo='Fsca', ano=1975, cor='Preto')
  print(meu_carro.obter_informacoes())
  
  meu_carro.acelerar(30)
  meu_carro.frear(10)
  
  print(meu_carro.obter_informacoes())
  print(meu_carro)  # Chama implicitamente o método __str__
```
>  **Classes não são objetos**: Classes definem o que um objeto do tipo "carro" precisa ter.


Neste exemplo, temos uma classe Carro com um construtor `__init__` que inicializa alguns atributos, como modelo, ano, cor e velocidade. A classe também possui métodos como `acelerar`, `frear` e `obter_informacoes`. O último método retorna uma string com informações sobre o carro.

> métodos são funções definidas dentro de classes

> `__init__` é um método especial, chamado de construtor.

A instância meu_carro é criada usando a classe Carro, e alguns métodos são chamados para modificar a velocidade do carro e obter informações sobre ele.

> usamos `self.algo` para que que a propriedade persista. Se for apenas declarada uma funcão simples, ela será apagada da memória depois que for utilizada.

> Usamos o padrão PascalCase para declarar classes 
>> `class DefinicaoDaClasseEmPascalCase`

No exemplo `from datetime import datetime` o primeiro datetime é o *módulo* e o segundo é uma *classe* dentro do módulo.