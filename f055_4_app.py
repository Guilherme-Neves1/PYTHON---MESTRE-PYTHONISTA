# **kwargs(Keyword argumentos) => Argumentos nomeados
'''
def concatenar(**palavras):
  frase = ''
  for palavra in palavras.values():
    frase += palavra + ' '
  print(frase)

concatenar(a='Nós', b='somos', c='Pythonistas', d='profissionais')
'''

# Exemplo
def fazer_calculos(nome, *args, **kwargs):
  print(nome)
  print(args)
  print(kwargs)
  for arg in args:
    print(arg)
  for kwarg in kwargs.values():
    print(kwarg)

fazer_calculos("Franklyn", 1, 2, 3, 4, a=5, b=6, c=7, d=8)