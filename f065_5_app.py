# Tuplas
## São uma maneira de armazenar valores que devem ser alterados.

# PARA NÃO PRECISAR FAZER:
'''
site1 = 'youtube.com'
site2 = 'google.com'
site3 = 'facebook.com'

ou

valor1 = 25
valor2 = 33
valor3 = 54
'''

# PODEMOS USAR AS TUPLAS
sites = ('youtube.com', 'google.com', 'facebook.com')
valores = (25, 33, 54, False)

print(sites[2])
print(valores[0])

# Os valores não podem ser alterados
# sites[1] = 'instagram.com' => Erro

# União de tuplas
dados_do_sistema = sites + valores
print(dados_do_sistema)

# Acesso de valores em uma tupla
print(dados_do_sistema[2])

print(sites)
print(valores)
