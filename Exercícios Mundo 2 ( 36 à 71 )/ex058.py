"""
    Exercício 58

    Melhore o jogo do DESAFIO 028 onde o computador vao "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
"""

from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?!''')

acertou = False
numero_computador = randint(0, 10)
contador = 0

while not acertou:
    contador += 1
    numero = int(input('Qual é seu palpite? '))

    if numero == numero_computador:
        acertou = True
    else:
        if numero < numero_computador:
            print('Mais... Tente mais uma vez.')
        elif numero > numero_computador:
            print('Menos... Tente mais uma vez.')

print(f'Acertou com {contador} tentativas. Parabéns!')
