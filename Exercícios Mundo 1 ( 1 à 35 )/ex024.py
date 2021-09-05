"""
    Exercício 24

    Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra SANTOS.
"""

cidade = str(input('Informe a cidade: '))

cidade = cidade.strip().upper()
cidade = cidade.split()

if cidade[0] == 'SANTOS':
    print('A cidade começa com Santos.')
else:
    print('A cidade não começa com Santos.')
