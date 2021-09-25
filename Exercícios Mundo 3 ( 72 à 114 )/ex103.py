"""
    Exercício 103

    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.

O programa deverá ser capas de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gols(s) no campeonato.')


print('-'*30)
nome_jogador = str(input('Nome do Jogador: '))
gols_jogador = str(input('Número de Gols: '))

if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

if nome_jogador.strip() == '':
    ficha(gols=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)
