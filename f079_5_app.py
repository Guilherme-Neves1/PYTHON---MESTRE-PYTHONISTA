# TRY, EXCEPT e FINALLY
internet = None

try:
  print("Fazendo conexão com a " + internet)
except TypeError as erro:
  print("Não foi possível completar a sua compra. Verifique sua internet.")
finally:
  print("Desfazendo a compra!")

try:
  valor = int(input("Digite um valor: "))
  print(valor / 0)

except ZeroDivisionError as erro2:
  print("Não é possível dividir por zero!")

except ValueError as erro3:
  print("Favor digitar apenas números!")

finally:
  print("A operação foi cancelada.")
  