"""
    Exercício 91

    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)
             }

rank = list()
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(1)

print('\nRanking dos jogadores:')
rank = sorted(jogadores.items(),
              key=itemgetter(1), # itemgetter serviu para pegar referência apenas dos números e organizar com base neles
              reverse=True)

for i, v in enumerate(rank):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
