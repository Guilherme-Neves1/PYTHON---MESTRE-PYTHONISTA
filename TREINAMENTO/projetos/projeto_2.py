from turtle import Turtle

t = Turtle()
t.speed(1)

distancia = input("Para qual direção devemos ir? 'f:frente' ou 't:trás'? ")

while distancia == 'f':
  frente = int(input("Quantos pixels devemos movimentar para frente? "))
  rotacao = input("Rotacionar para d:direita, e:esquerda ou n:não rotacionar? ")

  if rotacao == 'd':
    rotacaoDireita = int(input("Quanto para a direita devemos rotacionar? "))
    t.right(rotacaoDireita)
    t.forward(frente)

  elif rotacao == 'e':
    rotacaoEsquerda = int(input("Quanto para a esquerda devemos rotacionar? "))
    t.left(rotacaoEsquerda)
    t.forward(frente)

  else:
    t.forward(frente)

while distancia == 't':
  tras = int(input("Quantos pixels devemos movimentar para trás? "))
  rotacao = input("Rotacionar para d:direita, e:esquerda ou n:não rotacionar? ")

  if rotacao == "d":
    rotacaoDireita = int(input("Quanto para a direita devemos rotacionar? "))
    t.right(rotacaoDireita)
    t.backward(tras)

  elif rotacao == "e":
    rotacaoEsquerda = int(input("Quanto para a esquerda devemos rotacionar? "))
    t.left(rotacaoEsquerda)
    t.backward(tras)
  else:
    t.backward(tras)

  continuar = input("Continuar andando? ")

'''
# Movimentar a turtle para frente
t.forward(100)

# Rotacionar em X graus para a direita
t.right(90)
t.forward(100)

# Rotacionar em X graus para a esquerda
t.left(90)
t.forward(100)

# Movimentar a turtle para trás
t.backward(200)
input(0)
'''







