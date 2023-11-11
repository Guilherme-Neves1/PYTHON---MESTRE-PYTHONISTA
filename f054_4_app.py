# *args => Iniciar o nome de um parâmetro com * faz com que esse parâmetro receba mais de um argumento. 

def somar(*valores, b):
  print(valores)
  for valor in valores:
    b += valor
  print(b)

somar(5, 10, 15, 20, b=5)
