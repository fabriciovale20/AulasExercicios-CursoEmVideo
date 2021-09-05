"""
    Exercício 51

    Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.
"""

print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(0, 10):
    print(primeiro_termo, end=' → ')
    primeiro_termo += razao

print('ACABOU')
