# Flask 
 
 - É um micro framework para criar aplicativos web
 - WSGI

 Para criar o ambiente virtual

 ```
 py -3 -m venv .venv
 ```
 Ativando

 ```
 .\.venv\Scripts\activate
 ```
Instalando o flask no projeto
```
pip install flask
```

Para executar o arquivo `.app.py` e levantar o servidor local não usamos o comando python, e sim, flask:

```
flask --app app run
```

Agora a api está rodando no localhost.

# Desenvolvendo a API

Vamos usar as seguintes bibliotecas 

```python
import urllib.request, json
```

Conectando com a Rick and Morty API:

```python
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    # transformando characters em formato json
    char_dic = json.loads(characters)

    characters = []

    for character in char_dic["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }
        characters.append(character)
    return characters
```

# Criando um template

 [Exercicio - Personagens Rick and Morty](./app.py)

