# Herança

Uma classe pode herdar os métodos e atributos de outra classe.

## Herança simples

Aqui, vamos definir uma classe Pessoa e em seguida, uma classe Estudante que herda todos os atributos e métodos de Pessoa (`class Estudante(Pessoa):`).

```python

# Pessoa é a nossa classe base
class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._tipo = 'Pessoa'

    def falar_oi(self):
        print('Oi! Meu nome é {}'.format(self._nome))

    def falar_tipo(self):
        print('Meu tipo é {}'.format(self._tipo))

pessoa = Pessoa('Naira')
pessoa.falar_oi()
pessoa.falar_tipo()
print()

# A classe estudante é derivada da classe Pessoa.
# Relação é: "Estudante" é uma "Pessoa"
class Estudante(Pessoa): # o nome da classe base vem em parênteses
    def __init__(self, name, curso):
        super().__init__(name) # chama o construtor da classe base
        self._curso = curso

    def falar_curso(self):
        print(f'Eu, {self._nome}, estudo o curso "{self._curso}"') # A propriedade self._nome é herdada da classe base
    
    def falar_tipo(self): # Sobrescreve a função original da classe Pessoa
        self._tipo = 'Estudante'
        return super().falar_tipo()

estudante = Estudante('Yasmin', 'Introdução ao Python')
estudante.falar_oi() # o método "falar_oi" é herdado da classe base
estudante.falar_tipo() # o método "falar_tipo" é herdado da classe base, e sobrescrito na classe derivada
estudante.falar_curso()
print()
```
Podemos testar se um objeto é de um determinado tipo em tempo de execução com as funções abaixo:

```python
print('O objeto estudante é uma instância da classe Estudante? ', isinstance(estudante, Estudante)) #True
print('O objeto estudante é uma instância da classe Pessoa? ', isinstance(estudante, Pessoa)) #True
print('A classe Estudante é uma sub-classe de Pessoa? ', issubclass(Estudante, Pessoa)) #True
print('A classe Pessoa é uma sub-classe de Estudante? ', issubclass(Pessoa, Estudante)) #False
```

### Herança transitiva


```python
class Trabalhador(Pessoa): # Trabalhador também herda de Pessoa
    def __init__(self, nome, profissao):
        super().__init__(nome) # chama o construtor da classe base
        self.__profissao = profissao # atributo privado - só pode ser acessado dentro da classe Trabalhador
        self._tipo = 'Trabalhador'

    def falar_profissao(self):
        print(f'Eu, {self._nome}, exerço a profissão "{self.__profissao}"')
    
    def falar_tipo(self): # Sobrescreve a função original da classe Pessoa
        return super().falar_tipo()

class Professor(Trabalhador): # Professor herda de Trabalhador
    def __init__(self, nome, disciplina):
        super().__init__(nome, 'Professor') # chama o construtor da classe base
        self.__disciplina = disciplina

    def falar_profissao(self):
        self.__profissao = 'Instrutora' # variáveis privadas não conseguem ser alteradas pela classe derivada
        return super().falar_profissao()

    def falar_disciplina(self):
        print(f'Eu, {self._nome}, dou aulas da disciplina "{self.__disciplina}"')
    
    def falar_tipo(self): # Sobrescreve a função original da classe Pessoa
        self._tipo = 'Professor'
        return super().falar_tipo()

trabalhadora = Trabalhador('Beatriz', 'Desenvolvedora')
trabalhadora.falar_oi()
trabalhadora.falar_tipo()
trabalhadora.falar_profissao()
print()

professora = Professor('Clarisse', 'Python')
professora.falar_oi()
professora.falar_tipo()
professora.falar_profissao()
professora.falar_disciplina()
print()
```

### Classe object


Em Python, todos as classes herdam implicitamente da *classe object*.

```python
class Humano:
    pass

# A classe Humano já começa com vários atributos e métodos
humano = Humano()
print(dir(humano))
print()

# Esses mesmos atributos e métodos existem nas classes que declaramos acima
print(dir(professora))
print()
```

## *Mixins* ou Herança múltipla

É uma funcionalidade avançada do python, mas que muitas vezes pode ser substituida por outras soluções mais simples. Raramente é usada, e deve ser evitada.


```python
class Logavel:
    def __init__(self):
        self.nome_da_classe = ''
    def logar(self, mensagem):
        print('Mensagem da classe ' + self.nome_da_classe + ': ' + mensagem)

class Conexao:
    def __init__(self):
        self.servidor = ''
    def conectar(self):
        print('Conectando ao banco de dados no servidor ' + self.servidor)
        # Lógica para realizar a conexão aqui

class MySqlDatabase(Conexao, Logavel):
    def __init__(self):
        super().__init__()
        self.nome_da_classe = 'MySqlDatabase'
        self.servidor = 'MeuServidor'

def framework(objeto):
    if isinstance(objeto, Conexao):
        objeto.conectar()
    if isinstance(objeto, Logavel):
        mensagem = 'Olá mulheres maravilhosas do Bootcamp de Python.'
        objeto.logar(mensagem)

conexao_mysql = MySqlDatabase()
framework(conexao_mysql)
```


- A classe *Logavel* define o método logar. Qualquer classe que herdar dela vai conseguir escrever uma mensagem no log e nós vamos saber de onde a mensagem está vindo pelo atributo nome_da_classe que é inicializado no construtor.
  - Ter uma classe assim é interessante porque a lógica de criar um arquivo de log, escrever as mensagens dentro dele e fechar o arquivo depois fica todo em um lugar só.
  - Quem está escrevendo um software não precisa se preocupar em escrever essa lógica toda vez, é só herdar de Logavel.
- A classe *Conexao* serve para conectar a um servidor de banco de dados.
  - O servidor costuma ser um endereço de IP com uma porta.
- A classe *MySqlDatabase* é uma classe de exemplo que se conecta ao banco de dados MySql, que herda tanto de conexão quanto de logável.
- O meu framework super chique aqui é só um metódo que recebe um objeto chamado item e testa se esse objeto é uma instância de cada uma das classes. Ele só chama os métodos pertinentes se for.