# Como pordemos criar listas no python?

# Laço de repetição(loops) com o Range()
numeros = []
for i in range(5):
  numeros.append(i)
print(numeros)

# Map
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']
def aprovar_pessoa(nome):
  # Pode-se fazer uma lógica mais complexa
  # Ex.: Verificar a pontuação do aluno em um banco de dados; Verificar se o pagamento foi feito em uma planilha etc.
  return nome + ' APROVADO'

print(list(map(aprovar_pessoa, nomes)))
