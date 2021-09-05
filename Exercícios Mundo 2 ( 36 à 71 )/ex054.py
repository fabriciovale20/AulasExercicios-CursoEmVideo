"""
    Exercício 54

    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

ano_atual = date.today().year
maior = menor = 0

for c in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = ano_atual - ano_nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'''
Ao todo tivemos {maior} pessoas maiores de idade.
E também tivemos {menor} pessoas menores de idade.
''')
