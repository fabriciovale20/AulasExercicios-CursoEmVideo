"""
    Exercício 88

    Faça um programa que ajude um jogar da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)

jogos = []
numeros = []

palpites = int(input('Quantos jogos você quer que eu sorteie? '))

for c in range(0, palpites):
    while True:
        n = randint(1, 60)
        if n not in numeros:
            numeros.append(n)
        if len(numeros) == 6:
            break
    jogos.append(numeros[:])
    numeros.clear()

print('=-'*3, f' SORTEANDO {palpites} JOGOS', '-='*3)

for c in range(0, len(jogos)):
    print(f'Jogo {c+1}: {sorted(jogos[c])}')
    sleep(1)

print('=-'*5, end=' < ')
print('{}'.format('BOA SORTE >'), end=' ')
print('-='*5)
