"""
    Exercício 69

    Crie um programa que leia a idade e o sexo de vároas pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:

a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
"""

homem = maior_de_18 = mulhers_menos_de_20 = 0

while True:
    print('-'*30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-'*30)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] '))

    # PESSOAS MAIORES DE 18 ANOS
    if idade > 18:
        maior_de_18 += 1

    # HOMENS CADASTRADOS
    if sexo in 'Mm':
        homem += 1
    else:
        # MULHER COM MENOS DE 20 ANOS
        if idade < 20:
            mulhers_menos_de_20 += 1

    resposta = str(input('Quer continuar? [S/N] '))
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N] '))

    if resposta in 'Nn':
        print('='*5, end='')
        print('{:^10}'.format(' FIM DO PROGRAMA '), end='')
        print('='*5)
        break

print(f'''
a) Total de pessoas com mais de 18 anos: {maior_de_18}
b) Ao todo temos {homem} homens cadastrados
c) E temos {mulhers_menos_de_20} mulheres com menos de 20 anos''')
