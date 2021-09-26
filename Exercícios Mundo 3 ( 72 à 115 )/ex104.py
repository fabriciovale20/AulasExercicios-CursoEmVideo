"""
    Exercício 104

    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
que fazendo a validação para aceitar apenas um valor numérico.

Ex:
n = leiaInt('Digite um número: ')
"""


def leiaInt(msg):
    while True:
        n = str(input(msg))

        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('\033[91mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
