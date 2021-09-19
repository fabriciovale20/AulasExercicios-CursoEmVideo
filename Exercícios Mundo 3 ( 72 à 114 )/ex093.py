"""
    Exercício 93

    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

gols = list()
for c in range(1, partidas+1):
    gols.append(int(input(f'    Quantos gols na {c}º partida? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print()

print(f'{" DICIONÁRIO ":-^40}')
print(jogador)
print()

print(f'{ "DADOS DO JOGADOR ":-^40}')
for k, v in jogador.items():
    print(f'O campo {k.title()} tem o valor {v}.')
print()

print(f'{" GOLS ":-^40}')
print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for i, v in enumerate(gols):
    print(f'    → Na {i+1}º partida, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
