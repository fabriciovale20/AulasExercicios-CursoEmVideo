"""
    Exercício 62

    Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programador encerra quando ele disser que quer mostrar 0 termos.
"""

print('='*30)
print('{:^30}'.format('GERADOR DE UMA PA'))
print('='*30)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

cont = 1
qnt_de_termos = 0

while cont <= 10:
    print(f'{primeiro_termo}', end=' → ')
    primeiro_termo += razao
    cont += 1
    qnt_de_termos += 1

print('ACABOU')

termos = 1
while termos != 0:
    termos = int(input('Quantos termos você quer mostrar a mais? '))
    if termos != 0:
        cont = 1
        while cont <= termos:
            print(f'{primeiro_termo}', end=' → ')
            primeiro_termo += razao
            cont += 1
            qnt_de_termos += 1
        print('ACABOU')

print(f'Progressão finalizada com {qnt_de_termos} termos mostrados.')
