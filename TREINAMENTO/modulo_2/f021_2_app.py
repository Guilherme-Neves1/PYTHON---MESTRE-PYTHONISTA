# Slice - extraindo partes de uma string

teclado = 'Teclado'
#          012 => Índice 
print(teclado[2]) # Índice 'c'
print(teclado.index('l')) # index busca o índice sem precisar contar
print(teclado[teclado.index('l')])

tecladodois = 'Teclado'

print(tecladodois[-1]) # -1 leva o índice à última letra

link = 'facebook.com/devaprender'
print(link[0])
print(link[-1])
print(link[0:5]) # Ele não inclui o último índice, neste caso a letra 'o'
print(link[0:])
print(link[-5])
print(link[5:])
print(link[:-5])

frase = 'Clean Code'
print(frase.rindex('C')) # índice do inicio até a última ocorrência de um caractere dentro de uma string

# DESAFIO 1
## Encontre o índice de 'o' dentro da varável biblioteca
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

# DESAFIO 2
## Usando a frase
###'Desenvolvimento De Aplicações'
## Imprima apenas a palavra 'De Aplicações'

# Tentativa
frase = 'Desenvolvimento De Aplicações'
print(frase[16:])

# Solução
indice_d = frase.rindex('D')
indice_s = frase.rindex('s')
print(frase[indice_d:indice_s+1])
