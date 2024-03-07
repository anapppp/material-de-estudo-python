# FastAPI

Possui métodos síncronos e assíncronos
Documentação automática

## Métodos síncronos em python

Usamos a biblioteca `asincio`. Um exemplo comum é fazer requisições HTTP assíncronas usando a biblioteca `aiohttp`.

```python
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url1 = 'https://jsonplaceholder.typicode.com/todos/1'
    url2 = 'https://jsonplaceholder.typicode.com/todos/2'

    # As chamadas a fetch_data são assíncronas, permitindo que outras tarefas sejam executadas enquanto aguardam a resposta
    task1 = asyncio.create_task(fetch_data(url1))
    task2 = asyncio.create_task(fetch_data(url2))

    # Espera que ambas as tarefas sejam concluídas
    data1 = await task1
    data2 = await task2

    print(f'Data from URL 1: {data1}')
    print(f'Data from URL 2: {data2}')

# Executa o loop de eventos assíncronos
asyncio.run(main())

```

Note que precisamos definir uma função ` async def main()`  e executá-la com `asyncio.run(main())`

## Executando um projeto em fastAPI

Criando um ambiente virtual

```
py -3 -m venv .venv
```
Ativando

```
.venv\Scripts\activate   
```

Instalando o fastAPI

```
pip install fastAPI["all"]
```

Executando com uvicorn 

```
uvicorn app:app --reload
```
> a vantagem do *uvicorn* é que voce nao precisa ficar reinicializando o servidor.

> O FastAPI usa a especificação OpenAPI e gera automaticamente a **documentação Swagger** para APIs RESTful. 
>> formato docs   http://127.0.0.1:8000/docs

>> formato redoc  http://127.0.0.1:8000/redoc 


## Métodos HTTP

```python

from fastapi import FastAPI, HTTPException

app = FastAPI()

# GET
@app.get("/")
async def root():
    return {"message": "Olá WoMakers!"}

@app.get("/api/users"):
async def get_users():
    return db;   #db foi criado anteriormente

@app.get("/api/users/{id}"):
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
        return {"message": "Usuario nao encontrado"}

# POST
@app.post("/api/users")
async def add_user(user:User):
    # Escreva um comentario em MarkDown para melhorar a Documentacao
    """
    Adiciona um usuario a base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    """
    db.append(user)
    return {"id": user.id}

# DELETE
@app.delete("/api/users/{id}")
async def remove_user(id:UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return   # Deixando assim sem nada, retorna soh o status 200
    raise HTTP(    #aqui tratamos as excecoes
        status_code=404,
        detail=f"Usuário com id {id} nao encontrado"
    )
```