from datetime import datetime

""" 
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data
lancamento_app = datetime(2021, 5, 28)
print(lancamento_app)

# Quero receber a data de lançamento do meu app
data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo?'),'%d/%m/%Y')
print(type(data_de_lancamento))

# Calcular o intervalo entre datas
data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)
"""

# DESAFIOS
## Calcule quantos dias faltam até o seu aniversário
# TENTATIVA
data_atual = datetime.now()
data_niver = datetime.strptime(input('Qual a data do seu aniversário? '),'%d/%m/%Y')

dias_prox_niver = data_niver - data_atual
print(dias_prox_niver)

# SOLUÇÃO
aniversario = datetime(2024, 8, 8)
dias_para_aniversario = aniversario - datetime.now()
print(dias_para_aniversario)
