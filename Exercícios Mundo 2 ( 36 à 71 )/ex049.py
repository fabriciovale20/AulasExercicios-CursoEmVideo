"""
    Exercício 49

    Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""

numero = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c}')
