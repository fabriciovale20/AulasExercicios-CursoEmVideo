"""
Exercício 06

    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

numero = int(input('Digite um número: '))

# Dobro
dobro = numero * 2
print(f'O dobro de {numero} é igual a {dobro}.')

# Triplo
triplo = numero * 3
print(f'O triplo de {numero} é igual a {triplo}.')

# Raiz quadrada
raiz = numero ** (1/2)
print(f'A raiz quadrada de {numero} é igual a {raiz:.2f}.')
