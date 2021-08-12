"""
Exercício 25

    Crie um programa que leia o nome de uma pessoa  diga se ela tem SILVA no nome.
"""

nome = str(input('Digite o nome completo: '))

if nome.upper().find('SILVA') == -1:
    print('Seu nome não tem SILVA.')
else:
    print('Seu nome tem SILVA.')
