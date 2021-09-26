"""
    Exercício 73

    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Uma lista com os times em ordem alfabética;
d) Em que posição na tabela está o time da Chapecoense.
"""

tupla = (
'Vasco', 'Flamengo', 'Botafogo', 'Chapecoense', 'Santos', 'Cruzeiro', 'Fluminense', 'Internacional', 'Potiguar', 'ABC')

print('5 Primeiros colocados')
for c in range(0, 5):
    print(f'{c + 1}º {tupla[c]}')

print('=' * 40)
print('Últimos 4 colocados')
for c in range(4, 0, -1):
    print(f'{len(tupla) - c + 1}º {tupla[-c]}')

print('=' * 40)
print('Times em ordem alfabética')
ordem = sorted(tupla)

for c in ordem:
    print(c, end=' - ')

print()
print('=' * 40)
print(f'O Chapecoense está na {tupla.index("Chapecoense") + 1}º posição')
