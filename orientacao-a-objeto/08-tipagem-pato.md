# Tipagem Pato (Duck Typing)

Python não usa um compilador, e sim, um *interpretador*, porque ele processa as informações na medida que o código é executado, e não, previamente, como em linguagens que são previamente compiladas. 

Como as variáveis não são tipadas, não é possível saber o tipo de uma variável em uma função.

```python
class Ave():
    def andar(self):
        print('andando')

    def voar(self):
        print('voando')

class Calopsita(Ave):
    def piar(self):
        print('piuuuu')

class Pato(Ave):
    def quack(self):
        print('quack')

    def nadar(self):
        print('nadando')

# A função não tem como garantir que o animal é de algum tipo específico, por exemplo, o tipo `Pato`
def executar_pato(animal):
    animal.quack()
    animal.andar()
    animal.voar()
    animal.nadar()

pato = Pato()
calopsita = Calopsita()

executar_pato(pato)   # execta normalmente
executar_pato(calopsita)   # retorna erro
```

Em Python, nós testamos em tempo de execução se o objeto tem tudo o que a gente espera. **O que importa para que um objeto seja considerado de uma determinada classe, é que esteobjeto tenha todos os métodos contidos naquela classe.**

> *Se andar como um pato, fazer quack como um pato e voar como um pato, então é um pato.*