"""
    Exercício 65

    Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
"""

media = maior = menor = cont = 0
resp = 'S'

while resp not in 'Nn':
    numero = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] '))
    if cont == 0:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

    media += numero
    cont += 1

print(f'''Você digitou {cont} números e a média foi {media / cont}
O maior valor foi de {maior} e o menor foi de {menor}''')
