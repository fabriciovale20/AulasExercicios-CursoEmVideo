"""
    Exercício 97

    Faça um programa que tenha uma função escreva() que receba um texto qualquer com parâmetro e mostre uma mensagem
com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~~~~~
  Olá, Mundo!
~~~~~~~~~~~~~~~
"""


def escreva(mensagem):
    letras = len(mensagem) + 4

    print('~'*letras)
    print(f'{mensagem:^{letras}}')
    print('~'*letras)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
