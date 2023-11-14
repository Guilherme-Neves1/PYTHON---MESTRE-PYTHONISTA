from datetime import datetime

def depositar_dinheiro():
    print("Depositando dinheiro")

    def depositando_dolar():
        print("Depositando dolares")

    def depositando_reais():
        print("Depositando reais")

    depositando_dolar()
    depositando_reais()

depositar_dinheiro()

# Exemplo 1
def pai(numero):
    def filho_1():
        print("Sou o filho 1")
    def filho_2():
        print("Sou o filho 2")
    if numero == 1:
        return filho_1
    
resultado = pai(1)
resultado()

# Decorators
