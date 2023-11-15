# ARRAYS

from array import array

# Inteiros, números decimais e caracteres
numeros = array('i',[1, 2, 3, 4, 5, 6, 7])
print(numeros)

# Adiciona um valor ao final da lista
numeros.append(10) 
print(numeros)

# Adiciona um valor no índice selecionado (índice 5 adiciona o número 200)
numeros.insert(5, 200)
print(numeros)

# Remove um valor que estiver no índice selecionado (nesse caso, 1)
numeros.pop(1)
print(numeros)

# Remove um valor diretamente, sem usar o índice
numeros.remove(5)
print(numeros)

# Também Remove um valor baseado no índice ou faixa selecionada
del numeros[1]
print(numeros)
