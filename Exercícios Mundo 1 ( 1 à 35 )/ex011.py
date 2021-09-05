"""
    Exercício 11

    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
    de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

print('----PINTAR PAREDE-----')

largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))

area = largura*altura
tinta = area/2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de \033[1:30m{area:.2f}m²\033[m.')
print(f'Para pintar essa parede, você precisará de \033[1:34m{tinta:.2f}L\033[m de tinta.')
