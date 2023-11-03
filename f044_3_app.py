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
