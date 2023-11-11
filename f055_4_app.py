# **kwargs(Keyword argumentos) => Argumentos nomeados
def concatenar(**palavras):
  frase = ''
  for palavra in palavras.values():
    frase += palavra + ' '
  print(frase)

concatenar(a='Nós', b='somos', c='Pythonistas', d='profissionais')