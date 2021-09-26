"""
    Exercício 76

    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma de tabular.
"""

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Carderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print('{:.<40}'.format(produtos[c]), end='')
    else:
        print('R$ {:>6.2f}'.format(produtos[c]))
