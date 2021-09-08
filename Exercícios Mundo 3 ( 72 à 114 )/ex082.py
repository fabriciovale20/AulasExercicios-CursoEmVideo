"""
    Exercício 82

    Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

valores = []
par = []
impar = []

while True:
    valores.append(int(input('Digite um número: ')))

    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper()

    if resposta == 'N':
        break

for c in valores:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print('-='*30)
print(f'''A lista completa é {sorted(valores)}
A lista de pares é {sorted(par)}
A Lista de ímpares é {sorted(impar)}''')
