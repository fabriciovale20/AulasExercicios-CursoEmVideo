"""
    Exercício 95

    Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""

jogadores = list()
dados = dict()

while True:
    print('-'*40)

    gols = list()
    gols.clear()

    dados.clear()

    dados['nome'] = str(input('Nome do Jogador: '))

    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na {c}º partida? ')))

    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print(jogadores)

print(f'{" ESTATÍSTICAS DOS JOGADORES ":-^50}')
print(f'{"Código":>5} {"Nome":<15} {"Gols":<10} {"Total":>10}')
for i, v in enumerate(jogadores):
    print(f'{i:^5} {v["nome"]:<15} {str(v["gols"]):<10} {v["total"]:>10}')

while True:
    print('-' * 40)
    buscar_jogador = int(input('Mostrar dados de qual jogador? '))

    if buscar_jogador == 999:
        print('<<< VOLTE SEMPRE >>>')
        break
    elif buscar_jogador >= len(jogadores) or buscar_jogador < 0:
        print(f'ERRO! Não existe jogador com código {buscar_jogador}! Tente novamente')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[buscar_jogador]["nome"]}')
        for i, v in enumerate(jogadores[buscar_jogador]['gols']):
            print(f'No jogo {i+1} fez {v} gols')
