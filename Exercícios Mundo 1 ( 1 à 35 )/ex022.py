"""
Exercício 22

    Crie um programa que leio o nome completo de uma pessoa e mostre:
a) Nome com todas as letras maiúsculas;
b) Nome com todas minúsculas;
c) Quantas letras no total(Sem considerar espaçõs);
d) Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite o nome completo: '))

# Nome com todas as letras maiúsculas
print(f'Nome com todas as letras maiúsculas: {nome.upper()}')

# Nome com todas minúsculas
print(f'Nome com todas minúsculas: {nome.lower()}')

# Quantas letras no total(Sem considerar espaçõs)
print(f'Quantas letras no total(Sem considerar espaçõs): {len(nome.replace(" ", ""))}')

# Quantas letras tem o primeiro nome
p = nome.split()
print(f'Quantas letras tem o primeiro nome: {p[0]} - {len(p[0])} letras')