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
