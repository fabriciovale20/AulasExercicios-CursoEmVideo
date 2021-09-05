"""
    Exercício 45

    Crie um programa que faça o computador jogar Jokenpô com você.
"""

import random

jogadas = ('Pedra', 'Papel', 'Tesoura')

print('''Suas opções:
1 - Pedra
2 - Papel
3 - Tesoura''')

opcao = int(input('Qual é a sua jogada? '))

computador = random.randint(1, 3)

print(f'''
-> Você escolheu {jogadas[opcao-1]}
-> Computador escolheu {jogadas[computador-1]}
''')

if opcao == computador:
    print('EMPATE')
elif opcao == 1:
    if computador == 2:
        print('Computador venceu!')
    else:
        print('Você venceu!')
elif opcao == 2:
    if computador == 1:
        print('Você venceu!')
    else:
        print('Computador venceu!')
elif opcao == 3:
    if computador == 1:
        print('Computador venceu!')
    else:
        print('Você venceu')
else:
    print('Jogada inválida!')
