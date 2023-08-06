
import requests
import json
import os

with open('Pokedex.json', 'r') as pokemon: # Abrir arquivo JSON
        Pokedex = json.load(pokemon)


#'https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png'

def salvar_img(url, name, destiny):
    try:
        resposta = requests.get(url)

        os.makedirs(destiny, exist_ok=True)

        c =  os.path.join(destiny,name)

        with open(c, 'wb') as arquivo: #salvamento do arquivo
            arquivo.write(resposta.content)
          
    except  Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

c = len(Pokedex)

for i in range(c):

    if i < 10:  
        salvar_img(f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/00{i}.png', f'{Pokedex[i]}-{i}.png','img')

    elif i < 100:
        salvar_img(f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/0{i}.png', f'{Pokedex[i]}-{i}.png','img')

    if i >= 100:
        salvar_img(f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/{i}.png', f'{Pokedex[i]}-{i}.png','img')

# ///
# //////////////////