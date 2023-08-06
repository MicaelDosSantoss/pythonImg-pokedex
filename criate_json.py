
import json
import requests

pokedex_nacional = 'https://pokeapi.co/api/v2/pokedex/1/'

get = requests.get(pokedex_nacional)  # GET para pegar a API
Pokedex_json = get.json() # Transformando o resultado do GET em JSON

pokedex_list = [['']]

for pokemon in Pokedex_json['pokemon_entries']:
    pokedex_list.append([
        pokemon["pokemon_species"]['name']
    ])

with open('Pokedex.json', 'w') as pokedex_json: 
    json.dump(pokedex_list, pokedex_json, indent=2)