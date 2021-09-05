"""
    Exercício 52

    Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

numero = int(input('Digite um número: '))
contador = 0

for c in range(1, numero+1):
    if numero % c == 0:
        contador += 1
        print(f'\033[93m{c}\033[m', end=' ')
    else:
        print(f'\033[91m{c}\033[m', end=' ')
print(f'''
O número {numero} foi divisível {contador} vezes
E por isso ele ''', end='')

if contador == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')
