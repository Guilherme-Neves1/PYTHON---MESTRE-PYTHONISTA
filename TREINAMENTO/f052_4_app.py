# Processar VS Retornar

## Função que apenas processa dados
#print("Olá!")

## Função que retorna dados
#cidade = input("Qual é a sua cidade? ")

# Como escolher entre funções que processam VS retornam dados?
## Basta se perguntar:
## Eu vou precisar usar essa informação na lógica do meu programa posteriormente? Ou só preciso processar esse dado, sem utilizá-lo depois

# ----------------PROCESSA DADOS-----------------------
'''
def exibir_cotacao_do_dia(moeda):
  if moeda == 'usd':
    print(5.47)

exibir_cotacao_do_dia('usd')
'''
# ----------------RETORNA DADOS-----------------------

def obter_cotacao_do_dia(moeda):
  if moeda == 'usd':
    return 5.57 # Semelhante ao input

cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
  print("Investir em ações americanas")
else:
  print("Cotação não favorável")
