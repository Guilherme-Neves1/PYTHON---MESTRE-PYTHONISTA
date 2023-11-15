# Loop while(laço while)

## Tentativas de colocar sua senha
'''
tentativas = 0
while tentativas < 3:
  print('Tente novamente.')
  tentativas += 1

# Senha
senha = ''
while senha != '123456':
  senha = input('Digite sua senha: \n')
print('Bem Vindo!')

# Receber o nome do usuário
nome = ''
while nome == '':
  nome = input('Digite seu nome: \n')
print(f'Bem vindo, {nome}')

# Ver o pôr do Sol às 17:00
horario = 0
while horario <= 17:
  print(horario)
  horario += 1
print('Hora de ir ver o pôr do Sol.')

# Contagem regressiva
contador = 100
while contador >= 0:
  print(contador)
  contador -= 1
'''

# DESAFIO 1
## Crie um loop while que irá contar e imprimir no console de 1 até 120.

num = 1
while num <= 120:
  print(f'{num}')
  num += 1

# DESAFIO 2
## Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'

senha = ''
while senha != 'secreto':
  senha = input('Digite a senha: \n')

# DESAFIO 3
## Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1.

valor = 100
while valor > 0:
  print(valor)
  valor -= 1
