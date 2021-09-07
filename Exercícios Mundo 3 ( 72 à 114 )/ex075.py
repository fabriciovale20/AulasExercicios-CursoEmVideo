"""
    Exercício 75

    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.
"""

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))
cont = 0

tupla = (a, b, c, d)


print(f'\nVocê digitou os valores {tupla}')

print(f'a) O valor 9 aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'b) O valor 3 apareceu na {tupla.index(3)+1}º posição')
else:
    print(f'b) O valor 3 não foi digitado em nenhuma posição')
print(f'c) Os valores pares digitados foram ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
