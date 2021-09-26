"""
    Exercício 78

    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
"""

lista = []

for c in range(0, 5):
    numero = int(input(f'Digite um valor para a Posição {c}: '))
    lista.append(numero)
    if c == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print('=-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, num in enumerate(lista):
    if num == maior:
        print(f'{pos}...', end=' ')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for pos, num in enumerate(lista):
    if num == menor:
        print(f'{pos}...', end=' ')
print()
