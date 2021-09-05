"""
    Exercício 60

    Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5x4x3x2x1 = 120
"""

numero = int(input('Digite um número para calcular seu fatorial: '))
fatoria = 1

print(f'Calculando {numero}! = ', end='')

while numero >= 1:
    if numero == 1:
        print(f'{numero} = ', end='')
    else:
        print(f'{numero} x ', end='')

    fatoria *= numero
    numero -= 1

print(fatoria)
