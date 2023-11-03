# Loop while(laço while)

## Tentativas de colocar sua senha
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
