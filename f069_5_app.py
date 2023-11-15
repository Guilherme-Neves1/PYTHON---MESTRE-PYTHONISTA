# Ordenar por propriedades
from operator import itemgetter

'''

nomes = ['Zack', 'Camilla', 'Julius', 'Romer']
valores = [31, 23, 6, 36, 21, 33, 37, 7, 20, 23]
pessoas = [
  {'nome': 'John',
   'idade': 32,
   'nivel_acesso': 2},

  {'nome': 'Carol',
   'idade': 18,
   'nivel_acesso': 3},

  {'nome': 'Thomas',
   'idade': 45,
   'nivel_acesso': 5},

  {'nome': 'Amanda',
   'idade': 23,
   'nivel_acesso': 1},
]

# Ordem crescente na lista simples

# nomes.sort()
# valores.sort()
# print(nomes)
# print(valores)

# Ordenar por propriedades uma lista de dicionário de pessoas
## Por nome
pessoas.sort(key=itemgetter('nome'))
print(pessoas)

print('----------------------------------------')
## Por nível de acesso
pessoas.sort(key=itemgetter('nivel_acesso'))
print(pessoas)

'''

'''
produtos = [
  ('Celular', 750),
  ('Bicicleta', 1500),
  ('Microfone', 550),
]

# Índice 1 = preço, então será ordenado em ordem crescente por preço
produtos.sort(key=itemgetter(1)) 
print(produtos)

# Índice 0 = nome, então será ordenado em ordem crescente por nome
produtos.sort(key=itemgetter(0)) 
print(produtos)

# ORDEM DECRESCENTE
produtos.sort(key=itemgetter(0), reverse=True) 
print(produtos)

matriz = [[5, 10], [15, 21], [1, 5]]
matriz.sort(key=itemgetter(1))
print(matriz)
'''

# DESAFIO 1 
## Ordene a lista de produtos abaixo pelo preço em ordem crescente
produtos = [
  {'nome': 'Celular',
   'preco': 1500
   },
  {'nome': 'Monitor',
   'preco': 600
   },
  {'nome': 'Microfone',
   'preco': 300
   },
]

produtos.sort(key=itemgetter('preco'))
print(produtos)

print(' ')
print(' ')
# DESAFIO 2
## Ordene em ordem decrescente a lista de equipamento_filmagem por valor
equipamento_filmagem = [
  ('Tripé', 300),
  ('Câmera', 1700),
  ('Iluminação', 200)
]

equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

print(' ')
print(' ')
# DESAFIO 3
## Ordene em ordem crescente a cotacao_moedas com base no valor da moeda
cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]

cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)
