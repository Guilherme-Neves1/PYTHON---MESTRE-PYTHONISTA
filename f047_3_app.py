from turtle import Turtle

# Inicializar uma turtle
t = Turtle()

# Definir uma velocidade
t.speed(1)
while True:
  distancia = int(input('Qual a distância a percorrer? '))
  t.forward(distancia)

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