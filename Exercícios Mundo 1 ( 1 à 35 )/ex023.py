"""
    Exercício 23

    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

numero = str(input('Digite um número: '))

digitos = len(numero)
numero = ' '.join(numero)
numero = numero.split()

if digitos == 1:
    print(f'Unidade: {numero[0]}')
elif digitos == 2:
    print(f'Unidade: {numero[1]}')
    print(f'Dezena: {numero[0]}')
elif digitos == 3:
    print(f'Unidade: {numero[2]}')
    print(f'Dezena: {numero[1]}')
    print(f'Centena: {numero[0]}')
elif digitos == 4:
    print(f'Unidade: {numero[3]}')
    print(f'Dezena: {numero[2]}')
    print(f'Centena: {numero[1]}')
    print(f'Milhar: {numero[0]}')
else:
    print('Contagem indisponível')
