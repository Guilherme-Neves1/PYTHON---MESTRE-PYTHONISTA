# Trabalhando com Múltiplas listas
from itertools import zip_longest

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
