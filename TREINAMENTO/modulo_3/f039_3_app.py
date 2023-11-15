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

# Método Chaining
velocidade = 100
if velocidade <= 50:
  print('Você não será multado.')
elif 51 <= velocidade <= 60:
  print('Você será multado em 2 pontos')
elif 61 <= velocidade <= 75:
  print('Você será multado em 3 pontos')
else:
  print('Você será multado em 7 pontos')

print('----------------------DESAFIO--------------------------')

# DESAFIO
## Cenário: Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguintes regras:
# * Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00.
# * Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00.
# * Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00.
# * Se seu cabelo estiver acima de 50cm, valor a combinar.

# Declare uma variável que represente o tamanho atual do seu cabelo.
tam_cabelo = 15
if tam_cabelo <= 20:
  print('O corte vai custar R$50,00.')

elif 21 <= tam_cabelo <= 30: # Chaining
# elif tam_cabelo >= 21 and tam_cabelo <= 30: # Forma comum
  print('O corte vai custar R$70,00.')

elif 31 <= tam_cabelo <= 50: # Chaining
# elif tam_cabelo >= 31 and tam_cabelo <= 50: # Forma comum
  print('O corte vai custar R$100,00.')

else: 
  print('O valor será a combinar na recepção.')

