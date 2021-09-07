"""
    Exercício 70

    Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre:

a) Qual é total gasto na compra.
b) Quantos produtos custam mais de R$1.000,00.
c) Qual é o nome do produto mais barato.
"""

print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)

total_compra = produto_maior_1000 = valor_produto_mais_barato = 0
nome_produto_mais_barato = ''

while True:
    nome_produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))

    # PRODUTO MAIS BARATO
    if total_compra == 0:
        nome_produto_mais_barato = nome_produto
        valor_produto_mais_barato = preco
    elif preco < valor_produto_mais_barato:
        nome_produto_mais_barato = nome_produto
        valor_produto_mais_barato = preco

    # TOTAL DA COMPRA
    total_compra += preco

    # PRODUTOS MAIOR QUE R$1.000,00
    if preco > 1000:
        produto_maior_1000 += 1

    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        print()
        print('-'*5, end='')
        print('{:^10}'.format(' FIM DO PROGRAMA '), end='')
        print('-'*5)
        break

print(f'''
a) O total da compra foi R${total_compra:.2f}
b) Temos {produto_maior_1000} custando mais de R$1.000,00
c) O produto mais barato foi {nome_produto_mais_barato} que custa {valor_produto_mais_barato:.2f}''')
