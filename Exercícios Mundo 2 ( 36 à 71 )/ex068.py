"""
    Exercício 68

    Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitóris consecutivas que ele conquistou no final do jogo.
"""

from random import randint

print('=-'*20)
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=-'*20)

venceu = 0

while True:
    numero = int(input('Digite um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper()

    computador = randint(0, 10)
    soma = numero + computador

    print('-'*30)
    print(f'Você jogou {numero} e o computador {computador}. Total de {soma} deu ', end='')

    if soma % 2 == 0:
        resultado = 'P'
        print('PAR')
    else:
        resultado = 'I'
        print('ÍMPAR')
    print('-' * 30)

    if resultado == opcao:
        venceu += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
    else:
        print('Você PERDEU!')
        break

print('=-'*20)
print(f'GAME OVER! Você venceu {venceu} vezes.')
