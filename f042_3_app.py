# Loop Aninhados
# País + estação
paises = ['Brasil', 'Índia', 'EUA', 'Egito']
estacoes_do_ano = ['Primavera', 'Verão', 'Outono', 'Inverno']

for pais in paises:
  for estacao in estacoes_do_ano:
    print(f'{pais} {estacao}')

for x in range(1, 11):
  for y in range(1, 6):
    print(f'Valor Externo {x} e Valor Interno {y}')

# DESAFIO