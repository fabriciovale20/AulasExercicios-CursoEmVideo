"""
    Exercício 61

    Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
"""

print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

cont = 1

while cont <= 10:
    print(f'{primeiro_termo}', end=' → ')
    primeiro_termo += razao
    cont += 1

print('ACABOU')
