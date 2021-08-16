"""
Exercício 28

    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from time import sleep
from random import randint

print('\033[1:93m-=\033[m'*28)
print('\033[1:94mVou pensar em um número entre 0 e 5. Tente adivinhar...\033/m')
print('\033[1:93m-=\033[m'*28)

numero_escolhido = randint(0, 5)

numero = int(input('Em que número eu pensei? '))

print('\033[1:95mPROCESSANDO', end='')
for c in range (0, 3):
    print('.', end='')
    sleep(0.5)

print()
if numero == numero_escolhido:
    print('\033[1:92mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[1:91mGANHEI! Eu pensei no número {numero_escolhido} e não no {numero}!')
