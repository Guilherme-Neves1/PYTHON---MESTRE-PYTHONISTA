# Continue => ignorar/pular
'''
for numero in range(100):
  if numero % 2 ==0:
    print(numero)
  else:
    continue

# Break => interromper a iteração
for numero in range(100):
  if numero % 2 ==0:
    print(numero)
  else:
    break

# Exemplo
frutas = ['maça', 'manga', 'morango', 'laranja']
for fruta in frutas:
  if fruta == 'manga':
    continue
  print(f'{fruta} adicionada a dieta.')
'''

# DESAFIO 1
## Ao chegar ao estilo 'Rap', o mesmo não deve ser impresso na tela.
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']

for estilo in estilos:
  if estilo == 'Rap':
    continue
  print(estilo)

# DESAFIO 2
## Use break ou continue para que a seguinte condição aconteça:
## Ao chegar em 'Rock', a execução deve parar.abs

for estilo in estilos:
  if estilo == 'Rock':
    break
  print(estilo)
