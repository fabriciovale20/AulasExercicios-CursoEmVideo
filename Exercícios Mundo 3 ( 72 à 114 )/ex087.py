"""
    Exercício 87

    Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha, coluna}: '))

print('=-'*30)
soma_par = soma_terceira_coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]
    print()

print('=-'*30)
print(f'''a) A soma dos valores pares é {soma_par}.
b) A soma dos valores da terceira coluna é {soma_terceira_coluna}.
c) O maior valor da segunda linha é {max(matriz[1])}.''')
