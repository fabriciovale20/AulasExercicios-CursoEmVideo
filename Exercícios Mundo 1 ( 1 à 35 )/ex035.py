"""
Exercício 35

    Desenvolva um programa que leia o comprimento de três restas e diga
ao usuário se elas podem ou não formar um triângulo.

Obs.: Para que seja possível formar um triângulo, a soma de dois lados
tem que ser maior que o lado.
"""

print('-='*20)
print('{:^40}'.format('Analisador de Triângulos'))
print('-='*20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os números formam um triângulo')
else:
    print('Os números \033[91mnão\033[m forma um triângulo')
