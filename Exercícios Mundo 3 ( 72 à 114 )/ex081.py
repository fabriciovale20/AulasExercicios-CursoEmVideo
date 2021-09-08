"""
    Exercício 81

    Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break

print('-='*30)
print(f'''a) Você digitou {len(lista)} elementos.
b) Os valores em ordem decrescente são {sorted(lista, reverse=True)}.''')

if 5 in lista:
    print('c) O valor 5 faz parte da lista.')
else:
    print('c) O valor 5 não foi encontrado na lista.')
