# MANIPULAR ITENS DAS LISTAS
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2050]

# Adicionar ao final da lista
valores.append(11) 
print(valores)

# Unir listas
valores.extend(anos)
print(valores)

# Adicionar listas
nova_lista = valores + anos
print(nova_lista)

# Inserir um novo valor: 2031 após 20304
print(anos[1])
anos.insert(2, 2031)
print(anos)

# Extrair com base no índice
anos_2040 = anos.pop(3)
print(anos_2040)

# Remover itens da lista
anos.remove(2050)
del anos[1]
del valores[1:7]
print(anos)
print(valores)
