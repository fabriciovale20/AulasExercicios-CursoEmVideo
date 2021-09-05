"""
    Exercício 42

    Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais;
- Isósceles: dois lados iguais;
- Escaleno: todos os lados diferentes
"""

print('-='*20)
print('{:^40}'.format('Analisador de Triângulos'))
print('-='*20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os números formam um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO.')
    elif a != b != c != a:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os números \033[91mnão\033[m forma um triângulo')
