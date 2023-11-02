# Conversão de tipos

# idade = input('Qual é a sua idade? ') => Erro pois o input por padrão transforma a resposta em string(str)
# idade = (input('Qual é a sua idade? '))
# print(int(idade) > 18) # Com o int convertemos o tipo

# print(type(str(5)))

# Receber valores decimais
altura_da_parede = input('Qual é a altura da parede? ')
# print(altura_da_parede > 2.10)
print(float(altura_da_parede) > 2.10)

# Algumas conversões que podemos fazer
int()
str()
float()
list()
tuple()
dict()
