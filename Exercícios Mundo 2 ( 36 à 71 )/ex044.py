"""
    Exercício 44

    Elabore um programa que calcule o valor a ser pago por um produto considerando
o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

print('='*10, end='')
print(' LOJAS GUANABARA ', end='')
print('='*10)

preco_compras = float(input('Preço das compras: R$'))
preco_compras_atual = preco_compras

print('''FORMAS DE PAGAMENTO
1 - à vista dinheiro/cheque
2 - à vista cartão
3 - 2x no cartão
4 - 3x ou mais no cartão
''')
forma_de_pagamento = int(input('Qual é a opção? '))

if forma_de_pagamento == 1:
    preco_compras_atual = preco_compras - (preco_compras * 0.1)
elif forma_de_pagamento == 2:
    preco_compras_atual = preco_compras - (preco_compras * 0.05)
elif forma_de_pagamento == 3:
    preco_compras_atual = preco_compras
    print(f'Sua compra será parcelada em 2x de R${preco_compras / 2:.2f}.')
elif forma_de_pagamento == 4:
    preco_compras_atual = preco_compras + (preco_compras * 0.2)

    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${(preco_compras_atual)/parcelas:.2f} COM JUROS')

print(f'Sua compra de R${preco_compras:.2f} vai custar R${preco_compras_atual:.2f} no final')
