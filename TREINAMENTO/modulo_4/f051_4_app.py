# FUNÇÕES
'''
input()
len()
split()
'''

# SINTAXE
'''

def nome_da_funcao(parametros):
  comandos

'''

# Exemplo 1
'''
def dar_boas_vindas():
  print("Bem-vindo!")

dar_boas_vindas()
'''

# Exemplo 2
'''
def dar_boas_vindas_personalizada(nome):
  print(f"Bem-vindo(a) {nome}")

dar_boas_vindas_personalizada("Guilherme")

# Também é possível passar mais parâmetros na função, porém devemos buscar usar poucos parâmetros por questão de boas práticas.

# def dar_boas_vindas_personalizada(nome, idade, tamanho):
'''

# Exemplo 3 - Valor padrão
'''
def apresentar_lugar(lugar="nossa loja"):
  print(f"Conheça {lugar}")

apresentar_lugar() # Mesmo vazio já foi definido o "lugar".

# apresentar_lugar("Disney") # O valor escrito aqui sobrepõe o já definido no def.
'''

# Exemplo 3.1
## Todo parâmetro que possuir valor padrão deve ser incluído ao final da lista de argumentos. Caso contrário, dá erro.
'''
def apresentar_lugar(horario_de_funcionamento, lugar="nossa loja"):
  print(f"Conheça {lugar}, horário de funcionamento das {horario_de_funcionamento}")

apresentar_lugar("08:00 às 18:00", "Disney") 
'''

# DESAFIO 1
## Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e o sobrenome de alguém e dá boas vindas para essa pessoa.
'''
def gerar_nome_completo(nome, sobrenome):
  print(f"Bem-vindo {nome} {sobrenome}!")

gerar_nome_completo("Guilherme", "Neves")
'''

# DESAFIO 2
## Crie uma função chamada calcular_valores que recebe 2 parâmetros, o primeiro sendo o preço de um produto e o segundo a quantidade deste produto, porém, a quantidade deve ter o valor padrão de '1'. Sua função deve exibir o preço do produto, multiplicando a quantidade que for escolhida.
def calcular_valores(pc_produto, qtd_produto=1):
  pc_final = pc_produto * qtd_produto
  print(f"O preço final do produto ficou: {pc_final}")

calcular_valores(30, 5)

# SOLUÇÃO DESAFIO 2
'''
def calcular_valores(preco, quantidade):
  print(preco * quantidade)

calcular_valores(30, 5)
'''