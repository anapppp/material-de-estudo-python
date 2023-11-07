# Métodos e Funções de listas

## Métodos de listas

> Métodos são chamados na forma `lista.metodo()`

Método | Descrição
--- | ---
`append(x)` | Adiciona o elemento x no final da lista.
`extend(iterable)` | Adiciona os elementos do iterável (como outra lista) no final da lista.
`insert(i, x)` | Insere o elemento x na posição i da lista.
`remove(x)` | Remove a primeira ocorrência do elemento x na lista.
`pop([i])` | Remove e retorna o elemento na posição i da lista. Se i não for especificado, remove e retorna o último elemento.
`index(x)` | Retorna o índice da primeira ocorrência do elemento x na lista.
`count(x)` | Retorna o número de ocorrências do elemento x na lista.
`sort(key=None, reverse=False)` | Ordena os elementos da lista (em ordem ascendente por padrão). O argumento key pode ser usado para especificar uma função de ordenação personalizada.
`reverse()` | Inverte a ordem dos elementos na lista.
`copy()` | Retorna uma cópia rasa da lista.

## Funções de listas

> Funcoes são chamadas na forma `funcao(lista)`

Função | Descrição
--- | ---
`len(lista)` | Retorna o número de elementos na lista. 
`min(lista)` | Retorna o menor elemento da lista.
`max(lista)` | Retorna o maior elemento da lista.
`sum(lista)` | Retorna a soma de todos os elementos da lista.
`sorted(lista)` | Retorna uma nova lista ordenada a partir dos elementos da lista.
`any(lista)` | Retorna True se pelo menos um elemento da lista for verdadeiro.
`all(lista)` | Retorna True se todos os elementos da lista forem verdadeiros.
`enumerate(lista)` | Retorna um objeto enumerado, que contém pares de índice e valor para cada elemento da lista.
`zip(lista1, lista2, ...)` |  Combina elementos correspondentes de várias listas em tuplas.
`map(funcao, lista)` | Aplica a função a todos os elementos da lista.
`filter(funcao, lista)` | Retorna uma lista contendo apenas os elementos para os quais a função retorna True.
`list(range(inicio, fim, passo))` | Gera uma lista de números no intervalo especificado.
