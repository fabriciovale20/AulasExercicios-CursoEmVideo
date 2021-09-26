"""
    Exercício 98

    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize
a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2;
c) Uma contagem personalizada.
"""

from time import sleep


def contador(inicio, fim, passo):
    passo = abs(passo)
    if passo == 0:
        passo = 1

    print('=-'*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ')
            sleep(0.5)
    else:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)

print('=-'*20)
print('Agora é sua vez de personalizar a contagem: ')
definir_inicio = int(input('Início: '))
definir_fim = int(input('Fim:    '))
definir_passo = abs(int(input('Passo:  ')))  # Utilizado abs() para pegar o valor absoluto sem o sinal de negativo

contador(definir_inicio, definir_fim, definir_passo)
