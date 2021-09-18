"""
    Exercício 80

    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutra na tela.
"""

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-'*40)

print(f'''Nome é igual a {aluno["nome"]}
Média é igual a {aluno["media"]:.1f}
Situação é igual a ''', end='')

if aluno['media'] >= 7:
    print('Aprovado')
elif 5 <= aluno['media'] < 7:
    print('Recuperação')
else:
    print('Reprovado')
