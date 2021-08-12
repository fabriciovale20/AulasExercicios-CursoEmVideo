"""
Exercício 72

    Crie um programa que tenha uma tupla preenchida com uma contagem
por extenso de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.
"""

tupla = (
'zero', 'um', 'dois', 'três', 'quartro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))
while numero > 10 or numero < 0:
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(tupla[numero].title())
