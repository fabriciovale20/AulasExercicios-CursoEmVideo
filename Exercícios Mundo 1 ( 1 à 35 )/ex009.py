"""
Exercício 09

    Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

numero = int(input('Digite um número para ver sua tabuada: '))

# Utilizando FOR
for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c}')
