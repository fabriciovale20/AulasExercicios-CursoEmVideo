"""
    Exercício 30

    Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR.
"""

numero = int(input('\033[95mMe diga um número qualquer:\033[m '))

print(f'O número {numero} ', end='')
if numero % 2 == 0:
    print('\033[94mPAR\033[m.')
else:
    print('\033[93mÍMPAR\033[m.')
