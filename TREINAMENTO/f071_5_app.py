# Filter
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']

def pessoa_aprovada(pessoa):
  if pessoa == 'Marcus':
    return True
  else:
    return False
  
print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes))) # Processa todos os dados

# Se precisamos processar todos os dados de uma lista ou de uma coleção usamos Map
# Se precisamos extrair apenas itens de uma condição específica usamos Filter

pinturas = [
  ['Pintura Clássica', 'Azul', 1857],
  ['Pintura Medieval', 'Vermelha', 1867],
  ['Pintura Moderna', 'Verde', 1897]
]

def eh_antiguidade(pintura):
  if pintura[2] < 1890:
    return True
  else:
    return False
  
print(list(filter(eh_antiguidade, pinturas)))
print(list(map(eh_antiguidade, pinturas)))

# DESAFIO 1
## Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500
vagas = [
  ['vaga 1', 1200],
  ['vaga 2', 2550],
  ['vaga 3', 5000]
]

def salario_maior_2500(salario):
  if salario[1] > 2500:
    return True
  else:
    return False
  
print(list(filter(salario_maior_2500, vagas)))
print(list(map(salario_maior_2500, vagas)))
