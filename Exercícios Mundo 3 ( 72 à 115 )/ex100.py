"""
    Exercício 100

    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores PARES sorteados pela função anterior.
"""

from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        numeros.append(randint(1, 10))

    for c in numeros:
        sleep(0.5)
        print(c, end=' ')
    print('PRONTO!')


def somapar():
    soma_par = 0

    for c in numeros:
        if c % 2 == 0:
            soma_par += c
    print(f'Somando os valores pares de {numeros}, temos {soma_par}.')


numeros = list()
sorteia()
somapar()
