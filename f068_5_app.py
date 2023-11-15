# Enumerate => Qual indice estamos iterando no momento

# Revendo aprendizados
'''
for numero in range(1, 11):
  print(numero)

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']
for nome in nomes:
  print(nome)
'''

# Com Enumerate, imprimindo os índices dos valores
## O '0' após o range indica que o índice inicial será 0, podendo ser qualquer valor.
'''
for indice, numero in enumerate(range(1, 11), 0):
  print(indice, numero)
  if indice == 5:
    print('Estamos na metade da lista')

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']
for indice, nome in enumerate(nomes, 1):
  print(indice, nome)
  if indice == 3:
    print('Já temos 3 pessoas registradas')
'''

# DESAFIO 1
## Itere sobre a lista abaixo exibindo o número do índice + nome da fruta.Porém quando o índice for 3 exiba 'Nº índice + nome da fruta EM PROMOÇÃO'
# frutas = ['Maça', 'Laranja', 'Morango', 'Limão']

frutas = ['Maça', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas, 0):
  print(indice, fruta)
  if indice == 3:
    print(f'{indice} {fruta} EM PROMOÇÃO')
