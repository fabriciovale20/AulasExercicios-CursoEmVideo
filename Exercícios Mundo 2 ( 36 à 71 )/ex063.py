"""
    Exercício 63

    Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma Sequência de Fibonacci.

Exemplo: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print('-'*40)
print('{:^40}'.format('Sequência de Fibonacci'))
print('-'*40)

numero = int(input('Quantos termos você quer mostrar? '))
print('~'*40)

anterior = 0
atual = 1

print(f'{anterior} → {atual}', end='')

cont = 3
while cont <= numero:
    proximo = anterior + atual
    print(f' → {proximo}', end='')
    anterior = atual
    atual = proximo
    cont += 1

print(' → FIM')
