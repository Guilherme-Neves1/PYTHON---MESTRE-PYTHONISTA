# Comparação com Operador Ternário
## Caso a idade seja maior ou igual a 18 anos, essa pessoa é maior de idade, caso contrário ela é menor de idade

# idade = 15
# if idade >= 18:
#   print('Maior de idade')
# else:
#   print('Menor de idade')

# Operador Ternário
idade = 25
print('Maior de idade') if idade >= 18 else print('Menor de idade')

# Sintaxe:
# Expressão IF Condição ELSE Expressão

possui_passaporte = False
print('Favor embarcar') if possui_passaporte == True else print('Favor tirar passaporte')

print('--------------------------DESAFIO--------------------------')

# DESAFIO
## Use a expressão condicional(Operador Ternário) para criar a seguinte condição
### * Se a velocidade estiver acima de 100, exibir: "Você foi multado".Caso contrário exiba siga em frente.
### Declare uma variável com o valor de 80.

velocidade = 80
print('Você foi multado') if velocidade > 100 else print('Você não foi multado')