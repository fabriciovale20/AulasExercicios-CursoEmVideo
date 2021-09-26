"""
    Exercício 89

    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

alunos = list()

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    alunos.append([nome, [n1, n2], media])

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('=-'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('FINALIZAND...')
        break
    if opcao <= len(alunos)-1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')
