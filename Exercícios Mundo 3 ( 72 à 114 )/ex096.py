"""
    Exercício 96

    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (larguna e
comprimento) e mostre a área do terreno.
"""

def area(largura, comprimento):
    area_total = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area_total:.1f}m².')


print('  Controle de Terrenos')
print('-' * 25)

largura = float(input('LARGUNA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)
