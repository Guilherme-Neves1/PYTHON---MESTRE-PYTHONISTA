# OBJETIVO
## Criar um módulo de login de um aplicativo e obter as segintes informações do funcionário.

# Módulo 1 - Gerar registro do funcionário
## 1. Obtenha o nome do usuário
## 2. Obtenha a idade do usuário
## 3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro.
## 4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
# cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
## 5. Guarde informações sobre a data de aniversário do funcionário

from datetime import datetime
import random

nome_usu = (str(input('Qual o seu nome? ')))
idade_usu = datetime.strptime(input('Qual a data do seu aniversário? '), '%d/%m/%Y')

cadastro = datetime.now()
print(cadastro)

cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
print(random.choice(cartoes))

# Módulo 2 - Gerar apresentação do usuário
## Usando os dados obtidos anteriormente, exiba a seguinte mensagem de boas vindas:
## 1. Olá (nome do usu), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa). Parabéns, houve um sorteio e você ganhou um cartão de comprar no valor de (valor sorteado).

print(f'Olá {nome_usu}, seu registro foi concluído com sucesso no dia {cadastro}.\nParabéns, houve um sorteio e você ganhou um cartão de comprar no valor de {cartoes}.')
