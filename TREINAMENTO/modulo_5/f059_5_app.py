'''
# Ao invés de:
preco_1 = 10
preco_2 = 20
preco_3 = 30

# Posso fazer Listas:
precos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(precos[0]) # Acessar por índice

print(precos[precos.index(100)]) # Enconter o index

# Liatas no python são dinâmicas(aceitam qualquer tipo de dado)
itens = [1, 2, 5, 'Olá', 'Café', True, 20.1]
print(itens[4])

# Maneiras diferentes de gerar uma lista
# Multiplicação de valores(repetição)
lista_de_noves = [9] * 10
lista_de_nomes = ['nomes'] * 10
print(lista_de_noves)
print(lista_de_nomes)

# Usando gerar Range(sequência)
# 1 até 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)

# Gerar a partir de strings
print(list('Bem-vindo ao treinamento'))

# Lista de lista(matriz)
matriz_de_nomes = [['Carol',30], ['Marcus',50]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
'''

# DESAFIO 1
## Crie uma lista com os nomes dos objetos que você mais usa no dia a dia e imprima na tela.

objetos_cotidiano = ['Garrafa', 'Celular', 'Fone']
print(objetos_cotidiano)

# DESAFIO 2
## Usando apenas uma linha de código, crie uma lista de 10 a 131.

lista_numeros = list(range(10, 132))
print(lista_numeros)

# DESAFIO 3
## Imprima na tela o resultado da combinação da lista do desafio 1 e do desafio 2.
print(objetos_cotidiano + lista_numeros)

# DESAFIO 4
## Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos do desafio 1, mas agora dentro de cada item você vai colocar uma informação extra, coloque o valor em reais desse objeto também e imprima na tela.

listaMatriz = [['Garrafa', 50], ['Celular', 1500], ['Fone', 40]]
print(listaMatriz[1][1])
