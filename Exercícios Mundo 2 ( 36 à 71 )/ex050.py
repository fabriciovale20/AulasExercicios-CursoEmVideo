"""
    Exercício 50

    Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que
forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

soma_pares = 0
quantidade_numero_pares = 0

for c in range(0, 6):
    numero = int(input(f'Digite o {c+1} valor: '))
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_numero_pares += 1

print(f'Você informou {quantidade_numero_pares} números PARES e a soma foi {soma_pares}.')
