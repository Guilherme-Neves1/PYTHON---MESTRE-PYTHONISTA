# Comparação comm Operadores Booleanos

# Exemplo 1
ler = print

idade = 21
possui_convite = False
filho_do_dono = True
ler((idade >= 21) and (possui_convite == True))
ler(idade >= 21 or possui_convite == True)

# Idade maior que 21 e possuir convite ou se for filho do dono.
ler((idade > 21 and possui_convite == True) or (filho_do_dono == True))
ler('-----------------------------------------------------------------')

# Exemplo 2
maior_de_idade = True
possui_carteira_de_trabalho = True

# Você só pode trabalhar se for maior de idade e possuir carteira de trabalho
ler((maior_de_idade == True) and (possui_carteira_de_trabalho == True))
ler(maior_de_idade and possui_carteira_de_trabalho) # É a mesma coisa que a leitura de cima.

# Só contratamos pessoas que ainda não possuem veículo próprio, mas já possuam carteira de trabalho.
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False
ler((possui_carteira_de_trabalho == True) and (not possui_veiculo_proprio))
ler('-----------------------------DESAFIO-----------------------------------')

# DESAFIO
# Definir as seguintes variáveis como False e montar as condicionais.
possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

# Uma pessoa só pode viajar se possuir passaporte, tiver a passagem comprada e não for menor de idade.
ler((possui_passaporte == True and passagem_comprada == True) and menor_de_idade == False)
ler((possui_passaporte) and (passagem_comprada) and not menor_de_idade)

# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade.
ler((possui_passaporte == True) or (passagem_comprada == True) and (menor_de_idade == False))
ler((possui_passaporte or passagem_comprada) and not menor_de_idade) # Simplificado

# Uma pessoa só pode viajar se não possuir passaporte ou se tiver a passagem comprada e não for menor de idade.
ler((possui_passaporte == False) or (passagem_comprada == True) and (menor_de_idade == False))
ler((not possui_passaporte or passagem_comprada) and not menor_de_idade)

# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade.
ler((possui_passaporte == False or passagem_comprada == False) and (menor_de_idade == True))
ler((not possui_passaporte or not passagem_comprada) and menor_de_idade)

# Uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor de idade.
ler((possui_passaporte == True) and (passagem_comprada == True) and (menor_de_idade == False))
ler((possui_passaporte and passagem_comprada) and not menor_de_idade)
