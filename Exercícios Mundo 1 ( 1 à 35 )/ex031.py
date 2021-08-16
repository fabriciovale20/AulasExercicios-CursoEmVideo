"""
Exercício 31

    Desenvolva um programa que pergunte a distância de uma viagemem Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45
para viagens mais longas.
"""

distancia = int(input('Qual é a distância da sua viagem? '))
preco = distancia * 0.5

print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km.\n'
      f'E o preço da sua passagem será de \033[97mR${preco:.2f}\033[m.')
