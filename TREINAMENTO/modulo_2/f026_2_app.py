# Valores aleatórios com random
import random

# Gera um valor de 0.0 a 1.0
print(random.random())

# Gera um valor decimal de Valor Mínimo ao Valor Máximo
print(random.uniform(4, 10))

# Gera um valor aleatório inteiro de mínimo e máximo
print(random.randint(4, 10))

cores = ['verde', 'vermelho', 'azul']
#Escolher opção aleatória
print(random.choice(cores))

cartas_de_um_baralho = ['carta1', 'carta2', 'carta3', 'carta4']
# Embaralhar uma lista
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)

# DESAFIO 1
## Simular a opção de jogar uma moeda e resultar em cara ou coroa, Jogue as opções dentro de uma lista e depois imprima o resultado na tela.abs

# DESAFIO 2
## Fazer um sorteio entre 5 nomes e imprimir o nome sorteado na tela.

# DESAFIO 3
## Escolher aleatoriamente um número entre 10 e 100 e imprimir o valor na tela. 

moeda = ['Cara', 'Coroa']
print(random.choice(moeda))

nomes = ['Guilherme', 'João', 'Pedro', 'Paulo', 'Maria']
print(random.choice(nomes))

print(random.randint(10, 100))