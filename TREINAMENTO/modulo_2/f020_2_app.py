# Métodos mais comuns de strings

nome_curso = '  Edição de Vídeo '
#             012345 => Índice
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip()) # remove os espaços da frase
print(nome_curso.lstrip()) # remove apenas os espaços da esquerda
print(nome_curso.rstrip()) # remove apenas os espaços da direita
print(nome_curso.find('ção')) # mostra o índice da palavra 'ção', que neste caso é 5
print(nome_curso.replace('Vídeo', 'Música')) # Substitui a primeira palavra pela segunda
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))

# DESAFIO
## Através da criação de strings dinâmicos e os métodos de strings, crie as seguintes frases
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print('É melhor FEITO que PERFEITO')
print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')
