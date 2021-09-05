"""
    Exercício 47

    Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

# APENAS COM FOR
for c in range(0, 51, 2):
    print(c, end=' ')

# COM FOR E IF
for c in range(0, 51):
    if c % 2 == 0:
        print(c, end=' ')
