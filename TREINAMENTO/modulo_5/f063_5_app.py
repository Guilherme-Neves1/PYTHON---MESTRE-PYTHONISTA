# Trabalhando com Múltiplas listas
from itertools import zip_longest

'''
a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1, 2, 3, 4, 5, 6]

for a, b in zip(a_lista, b_lista):
  print(a)
  print(b)
  
produtos = ["produto1", 'produto2', 'produto3', 'produto4']
precos = [600, 1200, 300, 150]

for a, b in zip(produtos, precos):
  print(f'Salvando produto {a} com o preço de R$ {b}')

titulos = ['titulo1', 'titulo2', 'titulo3', 'titulo4']
descricoes = ['descricao1', 'descricao2', 'descricao3']
for titulo, descricao in zip_longest(titulos, descricoes):
  print(f'Encontramos o {titulo} com a descrição: {descricao}')
'''
  
# DESAFIO 1

## Usando as listas abaixo:
# produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
# precos = ['R$500,00', 'R$1500,00', 'R$ 280,00', 'R$40,00']

## Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas, porém a pesquisa foi encontrada em momentos diferentes, assim acabamos com duas listas diferentes. Você precisa criar uma mensagem que diz o nome e o valor do produto, como as mensagens abaixo:
# Produto: Produto 1 encontrado no valor de R$ 500,00
# Produto: Produto 2 encontrado no valor de R$ 1500,00
# ...

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$ 280,00', 'R$40,00']

for produto, preco in zip_longest(produtos, precos):
  print(f'Produto: {produto} encontrado no valor de R$ {preco}')
