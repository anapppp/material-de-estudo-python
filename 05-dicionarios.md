# Dicionários

Um dicionário é uma estrutura de dados que associa pares chave-valor. 

## Criando um dicionário

```python
# Criando um dicionário vazio
meu_dicionario = {}

# Adicionando elementos ao dicionário
meu_dicionario['chave1'] = 'valor1'
meu_dicionario['chave2'] = 42
meu_dicionario['outra_chave'] = [1, 2, 3]
```
> Dicionário resultante: {'chave1': 'valor1', 'chave2': 42, 'outra_chave': [1, 2, 3]}

Outra opção:

```python
meu_dicionario = {'chave1': 'valor1', 'chave2': 42, 'outra_chave': [1, 2, 3]}
```

## Acessar valores por chave

```python
valor = meu_dicionario['chave1']
```

## Verificar se uma chave está no dicionário

```python
if 'chave1' in meu_dicionario:
    print('A chave está no dicionário.')
```

## Remover um par chave-valor

```python
del meu_dicionario['chave1']
```

## Obter todas as chaves ou valores

```python
chaves = meu_dicionario.keys()
valores = meu_dicionario.values()
```

## Iterar sobre pares chave-valor

```python
for chave in meu_dicionario:
    print(meu_dicionario[chave])
```
Outra opção:
```python
for chave, valor in meu_dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')
```
