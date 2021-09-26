"""
    Exercício 84

    Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas maias pesadas.
c) Uma listagem com as pessoas mais leves.
"""

temp = []
principal = []

maior_peso = menor_peso = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(principal) == 0:
        maior_peso = menor_peso = temp[1]
    else:
        if temp[1] > maior_peso:
            maior_peso = temp[1]
        if temp[1] < menor_peso:
            menor_peso = temp[1]

    principal.append(temp[:])
    temp.clear()

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('=-'*30)
print(f'''a) Ao todo, você cadastrou {len(principal)} pessoas.
b) O maior peso foi de {maior_peso:.1f}Kg. Peso de ''', end='')
for pessoa in principal:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}]', end=' ')

print()
print(f'c) O menor peso foi de {menor_peso:.1f}Kg. Peso de ', end='')
for pessoa in principal:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}]', end=' ')
