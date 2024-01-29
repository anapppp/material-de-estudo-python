# Usando SQLite no Python

## Estrutura geral

```python
import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Comandos SQL aqui: 
cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

conexao.commit()
conexao.close()
```

> o arquivo *.py* deve estar no mesmo diretório do banco de dados `banco`.