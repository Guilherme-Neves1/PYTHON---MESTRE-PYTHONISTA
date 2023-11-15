for numero in range(1, 21, 2):
  print('carregando', numero)

# Primeiro núm.: Número que vai começar na contagem;
# Segundo núm.: Número acima do que vai terminar a contagem (Aparece o penúltimo);
# Terceito núm.: De quanto em quanto vai contar.

nomes = ['jeff', 'carl', 'jean', 'luke']
for nome in nomes: 
  print(nome)

print('---------------------DESAFIO 1-------------------------')
# DESAFIO 1
## Usando um loop, exiba na tela: "Estamos em X". Onde X é um valor iniciado em 18 e finaliazado em 110. 
for x in range(18, 111):
  # print('Estamos em', x)
  print(f'Estamos em {x}')

print('---------------------DESAFIO 2-------------------------')
# DESAFIO 2
## Você precisa de 10 passos para finalizar uma tarefa, exiba na tela, usando um loop for a seguinte frase "Realizando Passo X"
for passo in range(1, 11):
  # print('Realizando passo', y)
  print(f'Realizando passo {passo}')