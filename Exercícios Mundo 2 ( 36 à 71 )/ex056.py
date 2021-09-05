"""
    Exercício 56

    Desenvolva um programa que lia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
► A média de idade do grupo.
► Qual é o nome do homem mais velho.
► Quantas mulheres têm menos de 20 anos.
"""

soma_idade = 0
nome_mais_velho = ''
idade_mais_velho = 0
mulheres_menos_20_anos = 0
contador = 0

for c in range(1, 5):
    print('-'*5, end='')
    print(' {:^5} '.format(f'{c}º PESSSOA'), end='')
    print('-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma_idade += idade

    if sexo == 'M':
        contador += 1
        if contador == 1:
            nome_mais_velho = nome
            idade_mais_velho = idade
        elif idade > idade_mais_velho:
            nome_mais_velho = nome
            idade_mais_velho = idade
    elif sexo == 'F':
        if idade < 20:
            mulheres_menos_20_anos += 1

print(f'''
A média de idade do grupo é de {soma_idade / 4} anos.
O homem mais velho tem {idade_mais_velho} anos e se chama {nome_mais_velho}.
Ao todo são {mulheres_menos_20_anos} mulheres com menos de 20 anos.
''')
