# IF ELIF ELSE
# if CONDIÇÃO:
#   comandos a serem executados

# trabalho_terminado = False
# if trabalho_terminado == True:
#   print('Bora dar uma saída!')
# else:
#   print('Não posso sair agora.')

# numero_atrasos = 2
# if numero_atrasos >= 3:
#   print('Vá para a diretoria!')
# elif numero_atrasos == 2:
#   print('Essa é sua segunda falta')
# elif numero_atrasos == 1:
#   print('Essa é sua primeira falta')
# else:
#   print('Pode entrar')

'''
A velocidade máxima para essa rua é de 50km
* Cruzou entre 51 a 60km, levou multa de 2 pontos
* Cruzou entre 61 a 75km, levou multa de 3 pontos
* Cruzou acima de 75km, levou multa de 7 pontos
'''

# TENTATIVA
'''
velocidade = 75
if 51 == velocidade <= 60:
  print('Você ultrapassou o limite de velocidade e foi multado em 2 pontos')
elif 61 == velocidade <= 75:
  print('Você ultrapassou o limite de velocidade e foi multado em 3 pontos')
elif velocidade > 75:
  print('Você ultrapassou o limite de velocidade e foi multado em 7 pontos')
else:
  print('Você está na velocidade certa.')
'''

# SOLUÇÃO
velocidade = 49
if velocidade <= 50:
  print('Você não será multado.')
elif velocidade >= 51 and velocidade <= 60:
  print('Você será multado em 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
  print('Você será multado em 3 pontos')
else:
  print('Você será multado em 7 pontos')
