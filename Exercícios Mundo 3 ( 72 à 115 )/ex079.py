"""
    Exercício 79

    Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, mostre todos os valores únicos digitados,
em ordem crescente.
"""

valores = []

while True:
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
        print('Valor adiconado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resposta = str(input('Quer continuar? [S/N] '))
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N] '))

    if resposta in 'Nn':
        break

print('=-'*30)
print(f'Você digitou os valores {sorted(valores)}')
