from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)


@app.route('/')
def get_list_elements_page():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])


@app.route('/lista')
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
