"""
Exercício 12

    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""

preco = float(input('Qual é o preço do produto? R$'))

desconto = preco * 0.05

print(f'O produto de R${preco:.2f} com desconto de 5% ficou R${preco - desconto:.2f}')
