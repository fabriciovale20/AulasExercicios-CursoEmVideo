"""
    Exercício 55

    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
o maior e o menor peso lidos.
"""

maior_peso = menor_peso = 0

for c in range(1, 6):
    peso = float(input(f'Peso da {c}º pessoa: '))
    if c == 1:
        maior_peso = menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f'''
O maior peso lido foi de {maior_peso:.1f}Kg
O menor peso lido foi de {menor_peso:.1f}Kg
''')
