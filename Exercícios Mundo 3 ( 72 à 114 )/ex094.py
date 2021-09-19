"""
    Exercício 94

    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas;
b) A média de idade do grupo;
c) Uma lista com todas as mulheres;
d) Uma lista com todas as pessoas com idade acima da média.
"""

lista = list()
dados = dict()

soma_idade = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))

    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break

    dados['idade'] = int(input('Idade: '))
    soma_idade += dados['idade']

    lista.append(dados.copy())

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
    if resposta == 'N':
        break
print('-'*40)

media_idade = soma_idade/len(lista)

print(f'''► O grupo tem {len(lista)} pessoas.
► A média de idade é de {media_idade:5.2f} anos.''')

print(f'''► As mulheres cadastradas foram: ''', end='')
for v in lista:
    if v['sexo'] == 'F':
        print(v['nome'], end=' ')
print()

print(f'''► Lista das pessoas que estão acima da média: ''')
for i, v in enumerate(lista):
    if v['idade'] > media_idade:
        print(f'    -Nome = {v["nome"]}; Sexo = {v["sexo"]}; Idade = {v["idade"]} anos')

print('\n<<< ENCERRADO >>>')
