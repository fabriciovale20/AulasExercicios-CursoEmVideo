"""
    Exercício 10

    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
"""

n = float(input('Informe quanto você tem na carteira: '))
dolar = n/3.27
print(f'Com o \033[1:30mR${n}\033[m você pode comprar \033[1:34mU${dolar:.2f}\033[m.')
