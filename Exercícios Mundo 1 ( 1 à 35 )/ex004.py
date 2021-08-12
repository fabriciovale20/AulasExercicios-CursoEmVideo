"""
Exercício 04

    Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivos e todas as informações possíveis sobre eltexto.
"""

texto = str(input('Digite algo: '))

print('O tipo primitivo desse valor é ', type(texto))
print('Só tem espaços? ', texto.isspace())
print('É um número? ', texto.isnumeric())
print('É alfabético? ', texto.isalpha())
print('É alfanumérico? ', texto.isalnum())
print('Está em maiúscula? ', texto.isupper())
print('Está em minúscula?', texto.islower())
print('Está captalizada? ',texto.istitle())
