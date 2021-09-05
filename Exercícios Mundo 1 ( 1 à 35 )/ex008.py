"""
    Exercício 08

    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

valor = float(input('Distância em metros: '))

centimetros = valor * 100
milimetros = valor * 1000

print(f'A medida em {valor}m, corresponde a {centimetros}cm e {milimetros}mm.')
