# Continue => ignorar/pular
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