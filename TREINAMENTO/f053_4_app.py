def exibir_preco(*, nome_produto, preco):
  print(f"{nome_produto} está no valor de: {preco}")

# Argumentos posicionais => diretamente ligados à posição que foram definidos na função. 
#exibir_preco("Iphone", 5000) # Nesse caso a ordem importa.

# Argumentos nomeados
#exibir_preco(preco=5000, nome_produto="Iphone") # A ordem não importa.
# O * define para o usuário que todos os argumentos que virão posteriormente DEVEM ser nomeados.

# DESAFIO 1
## Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros: cor, altura e formato. A sua função deve apenas imprimir na tela o que foi passado para ela. Porém, ela deve saeguir as seguintes regras: 
# 1- O primeiro argumento deve ser posicional; 
# 2- Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados.

def gerar_objeto_personalizado(cor,*, altura, formato):
  print(cor, altura, formato)

gerar_objeto_personalizado("vermelho", formato="quadrado", altura=60.5)
