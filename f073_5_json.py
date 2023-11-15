# Arquivo JSON
import json

# Salvar o arquivo
from pathlib import Path

'''
carros = [
  {"Marca": "Nissan", "Preço": 45.000, "Cor": "Azul"},
  {"Marca": "Ford", "Preço": 75.000, "Cor": "Verde"},
  {"Marca": "BMW", "Preço": 117.000, "Cor": "Amarelo"}
]

carros_json = json.dumps(carros)
Path('carros.json').write_text(carros_json)
'''

'''
arquivo_carros_json = Path('carros.json').read_text()
arquivo_json = json.loads(arquivo_carros_json)


print(arquivo_json[0]['Marca'] + ' ' + str(arquivo_json[0]['Preço']))
print(arquivo_json[1]['Marca'] + ' ' + str(arquivo_json[1]['Preço']))
'''

# DESAFIO 1
# Encontrar e exibir na tela a 'ability' 'imposter'
'''
pikachu_json = json.dumps(pikachu)
Path('pikachu.json').write_text(pikachu_json)

arquivo_pikachu_json = Path('pikachu_json').read_text()
pikachu_json = json.loads(arquivo_pikachu_json)

print(pikachu_json['ability'] ['lightning-rod'])
'''

# SOLUÇÃO
pikachu_json = Path('pikachu.json').read_text()
resultado = json.loads(pikachu_json)
print(resultado['abilities'][1]['ability']['name'])
