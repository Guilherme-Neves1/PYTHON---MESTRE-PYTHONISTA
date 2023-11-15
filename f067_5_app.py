# Range(geradores)

'''
# Gera números de 0(se não for especificado) até 29(o valor definido não aparece, somente o anterior a ele)
 
print(type(range(30)))

for numero in range(30):
  print(numero)
'''

'''
# Range com valor inicial 10, até 29
for numero in range(10, 30):
  print(numero)
'''

# Range com step(pular) de 2 em 2
for numero in range(10, 30, 2):
  print(numero)

# Criar listas mais rapidamente
resultado = list(range(0, 201, 10))
print(resultado)
