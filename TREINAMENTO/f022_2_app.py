# SPLIT E JOIN

""" 
frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split())
print(frase.split(',')) # Separa frases a cada vírgula(o separador não é incluído no final)
print(frase.split('-')) # Separa frases a cada traço

nomes = 'jhonatan, rafael, carol, amanda, jefferson'
print(nomes.split())
print(nomes.split(','))

hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))

# Como concatenar(combinar) strings
hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))
 """

# DESAFIO 1
## Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1

# DESAFIO 2
## Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras 2

# DESAFIO 3
## Pegue o palavras1 e transforme elas na seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.

# DESAFIO 4
## Pegue o palavras2 e transforme elas na seguinte string: frase2 = "Jhonatan & Rafael & Carol & Camilla". Imprima o resultado no console.

frase1 = 'Desafio manipulaçao de strings'
frase2 = 'Jhonatan,Rafael,Carol,Camilla'

# TENTATIVA
print(frase1.split())
palavras1 = frase1.split()
print(','.join(palavras1))

print(frase2.split(','))
palavras2 = frase2.split(',')
print(' & '.join(palavras2))

# SOLUÇÃO
palavrasum = frase1.split()
palavrasdois = frase2.split(',')
print(','.join(palavrasum))
print(' & '.join(palavras2))
