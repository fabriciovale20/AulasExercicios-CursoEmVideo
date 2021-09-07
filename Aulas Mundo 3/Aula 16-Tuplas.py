# TUPLAS SÃO IMUTÁVEIS
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

# print(lanche)
# print(lanche[1])
# print(lanche[3])
# print(lanche[-2])
# print(lanche[1:3])
# print(lanche[2:])
# print(lanche[:2])
# print(lanche[-2:])
# print(lanche[-3:])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# EXEMPLO 1
# for comida in lanche:
#     print(f'Eu vou comer {comida}')

# EXEMPLO 2
# for cont in range(0, len(lanche)):
#     print(lanche[cont])

# EXEMPLO 3
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

# print('Comi pra caramba!')

# SORTED -> ORDEM ALFABÉTICA
# print(sorted(lanche))

# JUNTANDO DUAS TUPLAS
# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c)
# c = b + a
# print(c)
# print(c.count(5))  # Quantas vezes aparece um determinado valor
# print(c.index(5))  # Em que posição está o valor determinado, pega a primeira ocorrência
# print(c.index(5, 1))  # Primeiro valor é para buscar, o segundo é valor que determiando de onde irá começar a busca

# TUPLAS PODE TER VÁRIS TIPOS DE VALORES
pessoa = ('Gustavo', 39, 'M', 99.98)
print(pessoa)
del(pessoa)  # Comando para apagar a tupla ou outras variáveis
