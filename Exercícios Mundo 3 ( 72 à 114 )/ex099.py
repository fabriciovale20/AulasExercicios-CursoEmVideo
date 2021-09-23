"""
    Exercício 99

    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep


def maior(*valores):
    print('=-' * 25)
    print('Analisando os valores passados...')

    total_valores = len(valores)
    if total_valores > 0:
        for c in valores:
            print(c, end=' ')
            sleep(0.5)
        print(f'Fora informados {total_valores} valores ao todo.')
        print(f'O maior valor informado foi {max(valores)}')
    else:
        print('Não foram passados nenhum valor.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
