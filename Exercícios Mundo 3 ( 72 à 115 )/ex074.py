"""
    Exercício 74

    Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que está na tupla.
"""

from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end='')
for c in tupla:
    print(c, end=' ')

print()
print(f'O maior valor soteador foi {max(tupla)}')
print(f'O menor valor soteador foi {min(tupla)}')
